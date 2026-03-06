(() => {
  const getAppBase = () => {
    const parts = window.location.pathname.split("/").filter(Boolean);
    return parts.length ? `/${parts[0]}` : "";
  };

  const encodePath = (path) =>
    path.split("/").map(encodeURIComponent).join("/");

  const setEditMode = (enabled) => {
    const layout = document.querySelector(".classic-main-layout");
    if (layout) {
      layout.classList.toggle("classic-edit-mode", enabled);
    }
    document.body.classList.toggle("classic-edit-mode", enabled);
    queueClassicLayoutResize();
  };

  const updateClassicEditHeight = () => {
    const layout = document.querySelector(".classic-main-layout");
    if (!layout) return;

    const inEditMode =
      document.body.classList.contains("classic-edit-mode") ||
      layout.classList.contains("classic-edit-mode");

    if (!inEditMode) {
      layout.style.removeProperty("--classic-edit-height");
      return;
    }

    const viewportHeight = window.visualViewport?.height || window.innerHeight;
    const rect = layout.getBoundingClientRect();
    const bottomGap = 20;
    const availableHeight = Math.max(320, Math.floor(viewportHeight - rect.top - bottomGap));

    layout.style.setProperty("--classic-edit-height", `${availableHeight}px`);
  };

  let resizeFrame = null;
  const queueClassicLayoutResize = () => {
    if (resizeFrame) return;
    resizeFrame = window.requestAnimationFrame(() => {
      resizeFrame = null;
      updateClassicEditHeight();
    });
  };

  let currentApp = null;

  const renderEditLayout = (payload, view = 'files') => {
    const leftPanel = document.querySelector(".classic-left-panel");
    if (!leftPanel) return;

    currentApp = payload;
    setEditMode(true);

    const actionButtons = `
      <button class="btn-small classic-edit-action-btn ${view === 'files' ? 'active' : ''}" data-view="files">
        <i class="fas fa-file-code"></i> Files
      </button>
      <button class="btn-small classic-edit-action-btn ${view === 'databases' ? 'active' : ''}" data-view="databases">
        <i class="fas fa-database"></i> Databases
      </button>
      <button class="btn-small classic-edit-action-btn ${view === 'routes' ? 'active' : ''}" data-view="routes">
        <i class="fas fa-route"></i> Routes
      </button>
      <button class="btn-small classic-edit-action-btn ${view === 'tickets' ? 'active' : ''}" data-view="tickets">
        <i class="fas fa-ticket-alt"></i> Tickets
      </button>
    `;

    leftPanel.innerHTML = `
      <div class="classic-edit-panel">
        <div class="classic-edit-header">
          <h2 class="classic-edit-title">Edit: ${payload.name}</h2>
          <div class="classic-edit-actions">
            ${actionButtons}
            <button class="btn-small" data-classic-edit-gitlog><i class="fas fa-list"></i> Gitlog</button>
            <button class="btn-small" data-classic-edit-translations><i class="fas fa-language"></i> i18n+p11n</button>
            <button class="btn-small" data-classic-edit-back><i class="fas fa-arrow-left"></i> Back</button>
          </div>
        </div>
        <div class="classic-edit-content" data-edit-view="${view}">
          ${renderViewContent(payload, view)}
        </div>
      </div>
    `;

    queueClassicLayoutResize();
    setupEventListeners(payload);
  };

  const renderViewContent = (payload, view) => {
    switch (view) {
      case 'files':
        return renderFilesView(payload);
      case 'databases':
        return renderDatabasesView(payload);
      case 'routes':
        return renderRoutesView(payload);
      case 'tickets':
        return renderTicketsView(payload);
      default:
        return renderFilesView(payload);
    }
  };

  let aceEditor = null;

  // Track last opened file so we can reload + reopen after tree refresh
  let classicReopenFilePath = null;

  // Global dialog function accessible from all scopes
  const showConfirmDialog = (title, message, confirmText, cancelText) => {
    return new Promise((resolve) => {
      const dialog = document.createElement("div");
      dialog.className = "classic-confirm-dialog-overlay";
      dialog.innerHTML = `
        <div class="classic-confirm-dialog">
          <div class="classic-confirm-dialog-header">
            <h3>${title}</h3>
          </div>
          <div class="classic-confirm-dialog-content">
            <p>${message}</p>
          </div>
          <div class="classic-confirm-dialog-actions">
            <button class="btn-small btn-primary" data-confirm-action>${confirmText}</button>
            <button class="btn-small" data-confirm-cancel>${cancelText}</button>
          </div>
        </div>
      `;

      document.body.appendChild(dialog);

      const confirmBtn = dialog.querySelector("[data-confirm-action]");
      const cancelBtn = dialog.querySelector("[data-confirm-cancel]");

      const cleanup = () => {
        dialog.remove();
      };

      confirmBtn.addEventListener("click", () => {
        cleanup();
        resolve(true);
      });

      cancelBtn.addEventListener("click", () => {
        cleanup();
        resolve(false);
      });
    });
  };

  // Check if editor has unsaved changes
  const checkIfDirty = () => {
    if (!aceEditor) return false;
    const dirtyState = aceEditor.__classicDirtyState;
    return Boolean(dirtyState) &&
           aceEditor.getValue() !== dirtyState.lastLoadedText;
  };

  // Confirm if there are unsaved changes
  const confirmIfDirtyGlobal = async () => {
    if (!checkIfDirty()) {
      return true; // No unsaved changes, proceed
    }

    return showConfirmDialog(
      "Unsaved Changes",
      "You have unsaved changes in the current file. Do you want to lose these changes or keep editing the file?",
      "Lose Changes",
      "Keep Editing"
    );
  };

  // (FIX) Missing in current file: renderFilesView is referenced by renderViewContent()
  const renderFilesView = (payload) => {
    const sections = payload.sections || {};
    const sectionOrder = Object.keys(sections);

    // Build hierarchy: treat "" as root; top-level folders are children of ""
    const hierarchy = { "": [] };

    sectionOrder.forEach((section) => {
      if (!section) return; // root
      const parts = section.split("/");
      const parentPath = parts.length === 1 ? "" : parts.slice(0, -1).join("/");
      (hierarchy[parentPath] ||= []).push(section);
    });

    const createFolderTree = (folderPath, isRoot = false) => {
      const folderName = folderPath.split("/").pop() || "root";
      const files = sections[folderPath] || [];
      const children = hierarchy[folderPath] || [];
      const hasChildren = children.length > 0;

      if (isRoot) {
        let html = `<ul class="classic-folder-list classic-folder-root-list" data-folder-list="${folderPath}">`;

        if (files.length > 0) {
          html += files
            .map(
              (f) =>
                `<li><button class="btn-small" data-classic-file data-section="${folderPath}" data-file="${f}">${f}</button></li>`
            )
            .join("");
        }

        if (hasChildren) {
          children.forEach((childPath) => {
            html += createFolderTree(childPath, false);
          });
        }

        html += `</ul>`;
        return html;
      }

      let html = `<li class="classic-subfolder">
        <button class="classic-folder-toggle" type="button" data-folder="${folderPath}" ${
          files.length === 0 && !hasChildren ? 'data-empty-folder="true"' : ""
        }>
          <i class="fas fa-folder"></i> ${folderName}
        </button>
        <ul class="classic-folder-list" data-folder-list="${folderPath}">
      `;

      if (files.length > 0) {
        html += files
          .map(
            (f) =>
              `<li><button class="btn-small" data-classic-file data-section="${folderPath}" data-file="${f}">${f}</button></li>`
          )
          .join("");
      }

      if (hasChildren) {
        children.forEach((childPath) => {
          html += createFolderTree(childPath, false);
        });
      }

      html += `</ul></li>`;
      return html;
    };

    const rootHasAny =
      (sections[""]?.length || 0) + ((hierarchy[""] || []).length || 0);

    const sectionHtml = rootHasAny
      ? `
        <div class="classic-folder classic-folder-files-root" data-folder-section="">
          <button class="classic-folder-root-toggle" type="button" data-folder="">
            <i class="fas fa-folder"></i>
            <span>${payload.name}</span>
          </button>
          ${createFolderTree("", true)}
        </div>
      `
      : `<div>No files found.</div>`;

    return `
      <div class="classic-edit-files" data-classic-edit-files>
        ${sectionHtml}
      </div>
      <div class="classic-edit-editor">
        <div class="classic-ace-editor" data-classic-editor></div>
        <div class="classic-edit-status" data-classic-edit-status></div>
        <div class="classic-edit-editor-actions">
          <button class="btn-small" data-classic-save disabled><i class="fas fa-save"></i> Save File</button>
          <button class="btn-small" data-classic-reload disabled><i class="fas fa-sync-alt"></i> Reload</button>
          <button class="btn-small btn-delete" data-classic-delete disabled><i class="fas fa-trash"></i> Delete</button>
          <button class="btn-small" data-classic-add-file><i class="fas fa-plus"></i> Add File</button>
          <button class="btn-small" data-classic-add-folder><i class="fas fa-folder-plus"></i> Add Folder</button>
          <button class="btn-small" data-classic-upload-file><i class="fas fa-upload"></i> Upload New File</button>
        </div>
      </div>
    `;
  };

  const renderDatabasesView = (payload) => {
    return `
      <div style="padding: 20px; width: 100%;">
        <div data-db-breadcrumb></div>
        <div data-databases-container>Loading databases...</div>
      </div>
    `;
  };

  const renderRoutesView = (payload) => {
    return `
      <div style="padding: 20px; width: 100%;">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 10px;">
          <h3 style="margin: 0;">Routes for ${payload.name}</h3>
          <button class="btn-small" data-classic-routes-reload>
            <i class="fas fa-sync-alt"></i> Reload
          </button>
        </div>
        <div data-routes-container>Loading routes...</div>
      </div>
    `;
  };

  const renderTicketsView = (payload) => {
    return `
      <div style="padding: 20px; width: 100%;">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 10px;">
          <h3 style="margin: 0;">Tickets for ${payload.name}</h3>
          <div style="display: flex; align-items: center; gap: 8px;">
            <button class="btn-small" data-classic-tickets-reload>
              <i class="fas fa-sync-alt"></i> Reload
            </button>
            <button class="btn-small btn-delete" data-classic-tickets-clear>
              <i class="fas fa-trash"></i> Clear Tickets
            </button>
          </div>
        </div>
        <div data-tickets-container>Loading tickets...</div>
      </div>
    `;
  };

  const setupEventListeners = (payload) => {
    const leftPanel = document.querySelector(".classic-left-panel");
    if (!leftPanel) return;

    const view = leftPanel.querySelector("[data-edit-view]")?.dataset.editView;

    leftPanel.querySelectorAll("[data-view]").forEach((btn) => {
      btn.addEventListener("click", async (e) => {
        e.preventDefault();
        const shouldProceed = await confirmIfDirtyGlobal();
        if (!shouldProceed) return;

        const newView = btn.dataset.view;
        renderEditLayout(payload, newView);
        if (newView === "databases") loadDatabases(payload.name);
        if (newView === "routes") loadRoutes(payload.name);
        if (newView === "tickets") loadTickets(payload.name);
      });
    });

    const backBtn = leftPanel.querySelector("[data-classic-edit-back]");
    if (backBtn) {
      backBtn.addEventListener("click", async (e) => {
        e.preventDefault();
        const shouldProceed = await confirmIfDirtyGlobal();
        if (!shouldProceed) return;
        window.location.reload();
      });
    }

    const gitlogBtn = leftPanel.querySelector("[data-classic-edit-gitlog]");
    if (gitlogBtn) {
      gitlogBtn.addEventListener("click", (e) => {
        e.preventDefault();
        window.open(`../gitlog/${encodeURIComponent(payload.name)}`);
      });
    }

    const translationsBtn = leftPanel.querySelector("[data-classic-edit-translations]");
    if (translationsBtn) {
      translationsBtn.addEventListener("click", (e) => {
        e.preventDefault();
        window.open(`../translations/${encodeURIComponent(payload.name)}`);
      });
    }

    if (view === "files") setupFilesView(payload);
    if (view === "databases") loadDatabases(payload.name);
    if (view === "routes") {
      loadRoutes(payload.name);
      const routesReloadBtn = leftPanel.querySelector("[data-classic-routes-reload]");
      if (routesReloadBtn) {
        routesReloadBtn.addEventListener("click", (e) => {
          e.preventDefault();
          reloadAppRoutes(payload.name);
        });
      }
    }
    if (view === "tickets") {
      loadTickets(payload.name);
      const ticketsReloadBtn = leftPanel.querySelector("[data-classic-tickets-reload]");
      const ticketsClearBtn = leftPanel.querySelector("[data-classic-tickets-clear]");
      if (ticketsReloadBtn) {
        ticketsReloadBtn.addEventListener("click", (e) => {
          e.preventDefault();
          reloadTicketsForApp(payload.name);
        });
      }
      if (ticketsClearBtn) {
        ticketsClearBtn.addEventListener("click", (e) => {
          e.preventDefault();
          clearTicketsForApp(payload.name);
        });
      }
    }
  };

  const setupFilesView = (payload) => {
    const leftPanel = document.querySelector(".classic-left-panel");
    if (!leftPanel) return;

    window.classicRefreshCurrentFiles = async () => {
      const appBase = getAppBase();
      try {
        const res = await fetch(`${appBase}/app_detail/${encodeURIComponent(payload.name)}`);
        if (!res.ok) throw new Error("Refresh failed");
        const data = await res.json();
        if (data.status !== "success") throw new Error(data.message || "Refresh failed");
        renderEditLayout(data.payload, "files");
      } catch (err) {
        console.error("[Classic Theme] Refresh failed:", err);
      }
    };

    const editorEl = leftPanel.querySelector("[data-classic-editor]");
    const saveBtn = leftPanel.querySelector("[data-classic-save]");
    const reloadBtn = leftPanel.querySelector("[data-classic-reload]");
    const deleteBtn = leftPanel.querySelector("[data-classic-delete]");
    const addBtn = leftPanel.querySelector("[data-classic-add-file]");
    const addFolderBtn = leftPanel.querySelector("[data-classic-add-folder]");
    const uploadFileBtn = leftPanel.querySelector("[data-classic-upload-file]");
    const status = leftPanel.querySelector("[data-classic-edit-status]");

    // (Re)bind Ace if DOM changed
    if (editorEl) {
      if (aceEditor && aceEditor.container !== editorEl) {
        try { aceEditor.destroy(); } catch (_) {}
        aceEditor = null;
      }
      if (!aceEditor) {
        aceEditor = ace.edit(editorEl);
        aceEditor.setTheme("ace/theme/chrome");
        aceEditor.setOptions({ fontSize: "12px", showPrintMargin: false, wrap: true });
      }
    }

    const dirtyState =
      aceEditor &&
      (aceEditor.__classicDirtyState ||= { lastLoadedText: "", suppress: false });

    let currentFolder = "";
    let selectedFolder = null;
    let currentFilePath = null;
    let selectedFileElement = null;
    let selectedFolderElement = null;

    const clearSelection = () => {
      if (selectedFileElement) selectedFileElement.classList.remove("selected-file");
      if (selectedFolderElement) selectedFolderElement.classList.remove("selected-folder");
      selectedFileElement = null;
      selectedFolderElement = null;
    };

    const isDirty = () => {
      return Boolean(aceEditor) &&
             Boolean(dirtyState) &&
             aceEditor.getValue() !== dirtyState.lastLoadedText;
    };

    const confirmIfDirty = async () => {
      if (!isDirty()) {
        return true; // No unsaved changes, proceed
      }

      return showConfirmDialog(
        "Unsaved Changes",
        "You have unsaved changes in the current file. Do you want to lose these changes or keep editing the file?",
        "Lose Changes",
        "Keep Editing"
      );
    };

    const setDirtyUi = (dirty) => {
      if (!saveBtn) return;
      saveBtn.classList.toggle("classic-save-dirty", Boolean(dirty) && !saveBtn.disabled);
    };

    const disableSave = () => {
      if (!saveBtn) return;
      saveBtn.disabled = true;
      saveBtn.classList.remove("classic-save-dirty");
    };

    const disableReload = () => {
      if (reloadBtn) reloadBtn.disabled = true;
    };

    const clearEditor = () => {
      if (!aceEditor) return;
      if (dirtyState) dirtyState.suppress = true;
      aceEditor.setValue("", -1);
      if (dirtyState) {
        dirtyState.lastLoadedText = "";
        dirtyState.suppress = false;
      }
      setDirtyUi(false);
    };

    // Hook dirty tracking once
    if (aceEditor && !aceEditor.__classicDirtyHooked) {
      aceEditor.__classicDirtyHooked = true;
      aceEditor.session.on("change", () => {
        const state = aceEditor.__classicDirtyState;
        if (!state || state.suppress) return;
        setDirtyUi(aceEditor.getValue() !== state.lastLoadedText);
      });
    }

    const loadFile = async (section, file, buttonElement) => {
      selectedFolder = null;
      currentFolder = section || "";
      currentFilePath = null;

      clearSelection();
      if (buttonElement) {
        buttonElement.classList.add("selected-file");
        selectedFileElement = buttonElement;
      }

      const appBase = getAppBase();
      const filePath = section ? `${payload.name}/${section}/${file}` : `${payload.name}/${file}`;
      classicReopenFilePath = filePath;

      if (status) status.textContent = `Loading ${filePath}...`;
      disableSave();
      disableReload();
      if (deleteBtn) deleteBtn.disabled = true;

      try {
        const res = await fetch(`${appBase}/load/${encodePath(filePath)}`);
        if (!res.ok) throw new Error("Load failed");
        const data = await res.json();

        if (aceEditor) {
          const modelist = ace.require("ace/ext/modelist");
          aceEditor.session.setMode(modelist.getModeForPath(filePath).mode);

          if (dirtyState) dirtyState.suppress = true;
          if (dirtyState) dirtyState.lastLoadedText = data.payload || "";
          aceEditor.setValue(dirtyState ? dirtyState.lastLoadedText : (data.payload || ""), -1);
          if (dirtyState) dirtyState.suppress = false;

          setDirtyUi(false);
        }

        currentFilePath = filePath;
        if (status) status.textContent = filePath;
        if (saveBtn) saveBtn.disabled = false;
        if (reloadBtn) reloadBtn.disabled = false;
        if (deleteBtn) deleteBtn.disabled = false;
      } catch (err) {
        if (status) status.textContent = `Error: ${err.message}`;
      }
    };

    const selectFolderUi = (folder, buttonElement, labelPrefix) => {
      selectedFolder = folder;
      currentFolder = folder;
      currentFilePath = null;
      classicReopenFilePath = null;

      clearSelection();
      if (buttonElement) {
        buttonElement.classList.add("selected-folder");
        selectedFolderElement = buttonElement;
      }

      if (status) status.textContent = `${labelPrefix}: ${folder}`;
      disableSave();
      disableReload();
      if (deleteBtn) deleteBtn.disabled = false;
      clearEditor();
    };

    const saveFile = async () => {
      if (!currentFilePath || !aceEditor) return;

      const appBase = getAppBase();
      if (status) status.textContent = `Saving ${currentFilePath}...`;

      try {
        const res = await fetch(`${appBase}/save/${encodePath(currentFilePath)}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(aceEditor.getValue()),
        });
        if (!res.ok) throw new Error("Save failed");
        const data = await res.json();
        if (data.status !== "success") throw new Error(data.message || "Save failed");

        if (dirtyState) dirtyState.lastLoadedText = aceEditor.getValue();
        setDirtyUi(false);
        if (status) status.textContent = `Saved ${currentFilePath}`;
      } catch (err) {
        if (status) status.textContent = `Error: ${err.message}`;
      }
    };

    const deleteSelected = async () => {
      const appBase = getAppBase();

      // delete folder if folder selected and no file open
      if (!currentFilePath && selectedFolder != null) {
        const folderPath = `${payload.name}/${selectedFolder}`;
        if (!confirm(`Delete folder "${selectedFolder}"?`)) return;

        if (status) status.textContent = `Deleting folder: ${selectedFolder}...`;
        try {
          const res = await fetch(`${appBase}/delete/${encodePath(folderPath)}`, { method: "POST" });
          if (!res.ok) throw new Error("Delete failed");
          const data = await res.json();
          if (data.status !== "success") throw new Error(data.message || "Delete failed");

          // refresh tree after delete
          const res2 = await fetch(`${appBase}/app_detail/${encodeURIComponent(payload.name)}`);
          const data2 = await res2.json();
          if (data2.status === "success") renderEditLayout(data2.payload, "files");
        } catch (err) {
          if (status) status.textContent = `Error: ${err.message}`;
        }
        return;
      }

      // delete file
      if (!currentFilePath) return;
      if (!confirm(`Delete ${currentFilePath}?`)) return;

      if (status) status.textContent = `Deleting ${currentFilePath}...`;
      try {
        const res = await fetch(`${appBase}/delete/${encodePath(currentFilePath)}`, { method: "POST" });
        if (!res.ok) throw new Error("Delete failed");
        const data = await res.json();
        if (data.status !== "success") throw new Error(data.message || "Delete failed");

        clearEditor();
        currentFilePath = null;
        classicReopenFilePath = null;
        disableSave();
        disableReload();
        if (deleteBtn) deleteBtn.disabled = true;

        const res2 = await fetch(`${appBase}/app_detail/${encodeURIComponent(payload.name)}`);
        const data2 = await res2.json();
        if (data2.status === "success") renderEditLayout(data2.payload, "files");
      } catch (err) {
        if (status) status.textContent = `Error: ${err.message}`;
      }
    };

    const addFile = async () => {
      const hint = currentFolder ? ` in ${currentFolder}/` : " in root";
      const name = prompt(`Enter new file name${hint} (e.g., myfile.py):`);
      if (!name) return;

      const appBase = getAppBase();
      const fullPath = currentFolder ? `${currentFolder}/${name}` : name;

      if (status) status.textContent = `Creating file: ${fullPath}...`;
      try {
        const res = await fetch(
          `${appBase}/new_file/${encodeURIComponent(payload.name)}/${encodePath(fullPath)}`,
          { method: "POST" }
        );
        if (!res.ok) throw new Error("Create failed");
        const data = await res.json();
        if (data.status !== "success") throw new Error(data.message || "Create failed");

        const res2 = await fetch(`${appBase}/app_detail/${encodeURIComponent(payload.name)}`);
        const data2 = await res2.json();
        if (data2.status === "success") renderEditLayout(data2.payload, "files");
      } catch (err) {
        if (status) status.textContent = `Error: ${err.message}`;
      }
    };

    const addFolder = async () => {
      const hint = currentFolder ? ` in ${currentFolder}/` : " in root";
      const name = prompt(`Enter new folder name${hint} (e.g., newfolder):`);
      if (!name) return;

      const appBase = getAppBase();
      const fullPath = currentFolder ? `${currentFolder}/${name}` : name;

      if (status) status.textContent = `Creating folder: ${fullPath}...`;
      try {
        const res = await fetch(
          `${appBase}/new_file/${encodeURIComponent(payload.name)}/${encodePath(fullPath)}?folder=1`,
          { method: "POST" }
        );
        if (!res.ok) throw new Error("Create failed");
        const data = await res.json();
        if (data.status !== "success") throw new Error(data.message || "Create failed");

        const res2 = await fetch(`${appBase}/app_detail/${encodeURIComponent(payload.name)}`);
        const data2 = await res2.json();
        if (data2.status === "success") renderEditLayout(data2.payload, "files");
      } catch (err) {
        if (status) status.textContent = `Error: ${err.message}`;
      }
    };

    // Wire file clicks
    leftPanel.querySelectorAll("[data-classic-file]").forEach((btn) => {
      btn.addEventListener("click", async (e) => {
        e.preventDefault();
        const shouldProceed = await confirmIfDirty();
        if (shouldProceed) {
          loadFile(btn.dataset.section || "", btn.dataset.file, btn);
        }
      });
    });

    // Wire folder toggles
    leftPanel.querySelectorAll(".classic-folder-toggle").forEach((btn) => {
      btn.addEventListener("click", async (e) => {
        e.preventDefault();
        const folder = btn.dataset.folder || "";
        const isEmpty = btn.dataset.emptyFolder === "true";
        currentFolder = folder;

        if (isEmpty) {
          const shouldProceed = await confirmIfDirty();
          if (shouldProceed) {
            selectFolderUi(folder, btn, "Selected folder");
          }
          return;
        }

        const shouldProceed = await confirmIfDirty();
        if (shouldProceed) {
          const list = leftPanel.querySelector(`[data-folder-list="${folder}"]`);
          if (list) list.classList.toggle("collapsed");
          btn.classList.toggle("collapsed");
          selectFolderUi(folder, btn, "Current folder");
        }
      });
    });

    if (saveBtn) saveBtn.addEventListener("click", (e) => { e.preventDefault(); saveFile(); });
    if (deleteBtn) deleteBtn.addEventListener("click", (e) => { e.preventDefault(); deleteSelected(); });
    if (addBtn) addBtn.addEventListener("click", (e) => { e.preventDefault(); addFile(); });
    if (addFolderBtn) addFolderBtn.addEventListener("click", (e) => { e.preventDefault(); addFolder(); });
    if (uploadFileBtn) {
      uploadFileBtn.addEventListener("click", (e) => {
        e.preventDefault();
        const dashboardApp = window.py4webDashboardApp;
        if (!dashboardApp || typeof dashboardApp.upload_new_file !== "function") {
          if (status) status.textContent = "Error: Upload action is not available.";
          return;
        }
        dashboardApp.selected_app = { name: payload.name };
        dashboardApp.selected_folder = currentFolder
          ? `${payload.name}/${currentFolder}`
          : null;
        dashboardApp.upload_new_file();
      });
    }

    if (reloadBtn) {
      reloadBtn.addEventListener("click", async (e) => {
        e.preventDefault();
        const fileToReopen = classicReopenFilePath;
        if (!fileToReopen) return;

        const isDirtyFlag =
          Boolean(aceEditor) &&
          Boolean(dirtyState) &&
          aceEditor.getValue() !== dirtyState.lastLoadedText;

        if (isDirtyFlag) {
          const shouldProceed = await showConfirmDialog(
            "Discard Changes and Reload?",
            "Discard unsaved changes and reload from disk?",
            "Reload",
            "Cancel"
          );
          if (!shouldProceed) return;
        }

        const appBase = getAppBase();
        try {
          const res = await fetch(`${appBase}/app_detail/${encodeURIComponent(payload.name)}`);
          if (!res.ok) throw new Error("Reload failed");
          const data = await res.json();
          if (data.status !== "success") throw new Error(data.message || "Reload failed");

          classicReopenFilePath = fileToReopen;
          renderEditLayout(data.payload, "files");
        } catch (err) {
          if (status) status.textContent = `Error: ${err.message}`;
        }
      });
    }

    // Auto-select: reopen file after Reload, else prefer __init__.py, else first file
    setTimeout(() => {
      if (classicReopenFilePath) {
        const prefix = `${payload.name}/`;
        const rel = classicReopenFilePath.startsWith(prefix)
          ? classicReopenFilePath.slice(prefix.length)
          : classicReopenFilePath;

        const parts = rel.split("/");
        const file = parts.pop();
        const section = parts.join("/");

        const candidates = leftPanel.querySelectorAll("[data-classic-file]");
        for (const el of candidates) {
          if ((el.dataset.section || "") === (section || "") && el.dataset.file === file) {
            el.click();
            return;
          }
        }
      }

      const init = leftPanel.querySelector('[data-classic-file][data-file="__init__.py"]');
      if (init) { init.click(); return; }

      const first = leftPanel.querySelector("[data-classic-file]");
      if (first) first.click();
    }, 0);
  };

  // Re-add missing async loaders for non-files views
  const loadDatabases = async (appName) => {
    const container = document.querySelector("[data-databases-container]");
    const breadcrumb = document.querySelector("[data-db-breadcrumb]");
    if (!container) return;

    const appBase = getAppBase();
    try {
      const res = await fetch(`${appBase}/rest/${encodeURIComponent(appName)}`);
      const data = await res.json();

      if (data.status === "success" && data.databases) {
        if (data.databases.length === 0) {
          if (breadcrumb) breadcrumb.innerHTML = `<h3>Databases for ${appName}</h3>`;
          container.innerHTML = "<p>No databases found for this app.</p>";
          return;
        }

        if (breadcrumb) breadcrumb.innerHTML = `<h3>Databases for ${appName}</h3>`;
        
        // Flatten all tables from all databases
        const allTables = [];
        data.databases.forEach((db) => {
          db.tables.forEach((table) => {
            allTables.push({
              dbName: db.name,
              tableName: table.name,
              fields: table.fields,
            });
          });
        });

        if (allTables.length === 0) {
          container.innerHTML = "<p>No tables found in databases.</p>";
          return;
        }

        container.innerHTML = `
          <div class="classic-db-tables-list">
            ${allTables
              .map(
                (table) => `
              <div class="classic-db-table-row" data-db="${table.dbName}" data-table="${table.tableName}">
                <div class="classic-db-table-name">
                  <i class="fas fa-table"></i> ${table.dbName}.${table.tableName}
                </div>
                <div class="classic-db-table-fields">
                  ${table.fields.join(", ")}
                </div>
              </div>
            `
              )
              .join("")}
          </div>
        `;

        // Add click handlers to table rows
        container.querySelectorAll(".classic-db-table-row").forEach((row) => {
          row.addEventListener("click", () => {
            const dbName = row.getAttribute("data-db");
            const tableName = row.getAttribute("data-table");
            const dbadminUrl = `${appBase}/dbadmin/${encodeURIComponent(appName)}/${encodeURIComponent(dbName)}/${encodeURIComponent(tableName)}`;
            window.location.href = dbadminUrl;
          });
        });
      } else {
        if (breadcrumb) breadcrumb.innerHTML = `<h3>Databases for ${appName}</h3>`;
        container.innerHTML = "<p>Could not load databases.</p>";
      }
    } catch (err) {
      if (breadcrumb) breadcrumb.innerHTML = `<h3>Databases for ${appName}</h3>`;
      container.innerHTML = `<p>Error: ${err.message}</p>`;
    }
  };

  const loadRoutes = async (appName) => {
    const container = document.querySelector("[data-routes-container]");
    if (!container) return;

    const appBase = getAppBase();
    try {
      const res = await fetch(`${appBase}/routes`);
      const data = await res.json();

      if (data.status === "success" && data.payload) {
        const routes = data.payload[appName] || [];
        if (routes.length === 0) {
          container.innerHTML = "<p>No routes found for this app.</p>";
          return;
        }
        const routeSortState = { key: "rule", dir: "asc" };
        const metricKeys = new Set(["time", "calls", "errors"]);
        const formatMetric = (value) => {
          const numeric = Number(value);
          return Number.isFinite(numeric) ? numeric.toFixed(2) : "0.00";
        };
        const sortedRoutes = (routeList) => {
          const sortKey = routeSortState.key;
          const sortDir = routeSortState.dir === "asc" ? 1 : -1;
          return [...routeList].sort((left, right) => {
            let leftValue = left?.[sortKey];
            let rightValue = right?.[sortKey];
            if (metricKeys.has(sortKey)) {
              leftValue = Number(leftValue || 0);
              rightValue = Number(rightValue || 0);
            } else {
              leftValue = String(leftValue || "").toLowerCase();
              rightValue = String(rightValue || "").toLowerCase();
            }
            if (leftValue < rightValue) return -1 * sortDir;
            if (leftValue > rightValue) return 1 * sortDir;
            return 0;
          });
        };

        const sortMarker = (key) => {
          if (routeSortState.key !== key) return "";
          return routeSortState.dir === "asc" ? " ▲" : " ▼";
        };

        const renderRoutesTable = () => {
          const ordered = sortedRoutes(routes);
          container.innerHTML = `
            <div class="classic-routes-scroll">
              <table style="width: 100%; border-collapse: collapse;">
              <thead>
                <tr style="background: #e3e3e3;">
                  <th data-sort-key="rule" style="padding: 8px; border: 1px solid #b5b5b5; text-align: left; cursor: pointer;">Rule${sortMarker("rule")}</th>
                  <th data-sort-key="method" style="padding: 8px; border: 1px solid #b5b5b5; text-align: left; cursor: pointer;">Method${sortMarker("method")}</th>
                  <th data-sort-key="filename" style="padding: 8px; border: 1px solid #b5b5b5; text-align: left; cursor: pointer;">Filename${sortMarker("filename")}</th>
                  <th data-sort-key="action" style="padding: 8px; border: 1px solid #b5b5b5; text-align: left; cursor: pointer;">Action${sortMarker("action")}</th>
                  <th data-sort-key="time" style="padding: 8px; border: 1px solid #b5b5b5; text-align: left; cursor: pointer;">Time(s)${sortMarker("time")}</th>
                  <th data-sort-key="calls" style="padding: 8px; border: 1px solid #b5b5b5; text-align: left; cursor: pointer;">Calls/s${sortMarker("calls")}</th>
                  <th data-sort-key="errors" style="padding: 8px; border: 1px solid #b5b5b5; text-align: left; cursor: pointer;">Errors/s${sortMarker("errors")}</th>
                </tr>
              </thead>
              <tbody>
                ${ordered
                  .map(
                    (r) => `
                  <tr>
                    <td style="padding: 6px; border: 1px solid #b5b5b5;">
                      <a href="${r.rule}" target="_blank"><code>${r.rule}</code></a>
                    </td>
                    <td style="padding: 6px; border: 1px solid #b5b5b5;"><code>${r.method}</code></td>
                    <td style="padding: 6px; border: 1px solid #b5b5b5;"><code>${r.filename || ""}</code></td>
                    <td style="padding: 6px; border: 1px solid #b5b5b5;"><code>${r.action}</code></td>
                    <td style="padding: 6px; border: 1px solid #b5b5b5;"><code>${formatMetric(r.time)}</code></td>
                    <td style="padding: 6px; border: 1px solid #b5b5b5;"><code>${formatMetric(r.calls)}</code></td>
                    <td style="padding: 6px; border: 1px solid #b5b5b5;"><code>${formatMetric(r.errors)}</code></td>
                  </tr>
                `
                  )
                  .join("")}
              </tbody>
            </table>
            </div>
          `;

          container.querySelectorAll("th[data-sort-key]").forEach((header) => {
            header.addEventListener("click", () => {
              const key = header.getAttribute("data-sort-key");
              if (routeSortState.key === key) {
                routeSortState.dir = routeSortState.dir === "asc" ? "desc" : "asc";
              } else {
                routeSortState.key = key;
                routeSortState.dir = metricKeys.has(key) ? "desc" : "asc";
              }
              renderRoutesTable();
            });
          });
        };

        renderRoutesTable();
      } else {
        container.innerHTML = "<p>Could not load routes.</p>";
      }
    } catch (err) {
      container.innerHTML = `<p>Error: ${err.message}</p>`;
    }
  };

  const reloadAppRoutes = async (appName) => {
    const appBase = getAppBase();
    const button = document.querySelector("[data-classic-routes-reload]");
    const container = document.querySelector("[data-routes-container]");
    if (button) button.disabled = true;
    if (container) container.innerHTML = "<p>Reloading app routes...</p>";

    try {
      const res = await fetch(`${appBase}/reload/${encodeURIComponent(appName)}`);
      if (!res.ok) throw new Error("Reload failed");

      let payload = null;
      try {
        payload = await res.json();
      } catch (_err) {
        payload = null;
      }

      if (payload && payload.status === "error") {
        throw new Error(payload.message || "Reload failed");
      }

      await loadRoutes(appName);
    } catch (err) {
      if (container) {
        container.innerHTML = `<p>Error: ${err.message}</p>`;
      }
    } finally {
      if (button) button.disabled = false;
    }
  };

  const loadTickets = async (appName) => {
    const container = document.querySelector("[data-tickets-container]");
    if (!container) return;

    const appBase = getAppBase();
    try {
      const res = await fetch(`${appBase}/tickets`);
      const data = await res.json();

      if (data.status === "success" && data.payload) {
        const tickets = data.payload.filter((t) => t.app_name === appName);
        if (tickets.length === 0) {
          container.innerHTML = "<p>No tickets found for this app.</p>";
          return;
        }
        container.innerHTML = `
          <table style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr style="background: #e3e3e3;">
                <th style="padding: 8px; border: 1px solid #b5b5b5; text-align: left;">Count</th>
                <th style="padding: 8px; border: 1px solid #b5b5b5; text-align: left;">Error</th>
                <th style="padding: 8px; border: 1px solid #b5b5b5; text-align: left;">Path</th>
                <th style="padding: 8px; border: 1px solid #b5b5b5; text-align: left;">Timestamp</th>
              </tr>
            </thead>
            <tbody>
              ${tickets
                .map(
                  (t) => `
                <tr>
                  <td style="padding: 6px; border: 1px solid #b5b5b5;">${t.count}</td>
                  <td style="padding: 6px; border: 1px solid #b5b5b5;"><code>${t.error}</code></td>
                  <td style="padding: 6px; border: 1px solid #b5b5b5;"><code>${t.path}</code></td>
                  <td style="padding: 6px; border: 1px solid #b5b5b5;">${t.timestamp}</td>
                </tr>
              `
                )
                .join("")}
            </tbody>
          </table>
        `;
      } else {
        container.innerHTML = "<p>Could not load tickets.</p>";
      }
    } catch (err) {
      container.innerHTML = `<p>Error: ${err.message}</p>`;
    }
  };

  const reloadTicketsForApp = async (appName) => {
    const button = document.querySelector("[data-classic-tickets-reload]");
    const container = document.querySelector("[data-tickets-container]");
    if (button) button.disabled = true;
    if (container) container.innerHTML = "<p>Reloading tickets...</p>";

    try {
      await loadTickets(appName);
    } finally {
      if (button) button.disabled = false;
    }
  };

  const clearTicketsForApp = async (appName) => {
    const reloadButton = document.querySelector("[data-classic-tickets-reload]");
    const clearButton = document.querySelector("[data-classic-tickets-clear]");
    const container = document.querySelector("[data-tickets-container]");
    if (reloadButton) reloadButton.disabled = true;
    if (clearButton) clearButton.disabled = true;
    if (container) container.innerHTML = "<p>Clearing tickets...</p>";

    try {
      const appBase = getAppBase();
      const res = await fetch(`${appBase}/clear`);
      if (!res.ok) throw new Error("Clear tickets failed");
      await loadTickets(appName);
    } catch (err) {
      if (container) {
        container.innerHTML = `<p>Error: ${err.message}</p>`;
      }
    } finally {
      if (reloadButton) reloadButton.disabled = false;
      if (clearButton) clearButton.disabled = false;
    }
  };

  const handleEditClick = async (appName, view = 'files') => {
    if (!appName) return;
    const appBase = getAppBase();
    const editUrl = `${appBase}/app_detail/${encodeURIComponent(appName)}`;

    try {
      const res = await fetch(editUrl);
      if (!res.ok) throw new Error(`HTTP ${res.status}: ${res.statusText}`);
      const data = await res.json();
      if (data.status !== "success") throw new Error(data.message || "Request failed");
      renderEditLayout(data.payload, view);
    } catch (err) {
      console.error("[Classic Theme] Edit failed:", err);
      alert("Edit failed: " + err.message);
    }
  };

  window.addEventListener("resize", queueClassicLayoutResize);
  if (window.visualViewport) {
    window.visualViewport.addEventListener("resize", queueClassicLayoutResize);
  }

  window.classicEditHandler = handleEditClick;
})();
