/**
 * Modern Theme - Activity Bar Navigation
 * Provides VSCode-style Activity bar with app navigation
 */

// Configuration for Activity bar actions
function getDashboardBaseUrl() {
  if (window.DashboardThemeUtils && typeof window.DashboardThemeUtils.getDashboardBaseUrl === 'function') {
    return window.DashboardThemeUtils.getDashboardBaseUrl();
  }
  return window.location.origin + '/_dashboard';
}

function buildDashboardViewUrl(view) {
  const appName = getCurrentAppName();
  if (window.DashboardThemeUtils && typeof window.DashboardThemeUtils.getDashboardViewUrl === 'function') {
    return window.DashboardThemeUtils.getDashboardViewUrl(appName, view);
  }
  const target = new URL(getDashboardBaseUrl() + '/index');
  if (appName) {
    target.searchParams.set('app', appName);
  }
  if (view) {
    target.searchParams.set('view', view);
  }
  return target.toString();
}

let ticketBadgeReqSeq = 0;

function getDashboardRelativeBase() {
  if (window.DashboardThemeUtils && typeof window.DashboardThemeUtils.getDashboardRelativeBase === 'function') {
    return window.DashboardThemeUtils.getDashboardRelativeBase();
  }
  return '/_dashboard';
}

function clearTicketsBadge() {
  upsertTicketsBadge(0);
}

function upsertTicketsBadge(count) {
  const ticketsBtn = document.getElementById('activity-btn-tickets');
  if (!ticketsBtn) return;
  const safeCount = Number(count) || 0;
  const existing = ticketsBtn.querySelector('.activity-badge');
  const label = safeCount > 99 ? '99+' : String(safeCount);
  const applyBadgeState = (badgeEl) => {
    if (safeCount > 0) {
      badgeEl.textContent = label;
      badgeEl.classList.remove('empty');
    } else {
      badgeEl.textContent = '';
      badgeEl.classList.add('empty');
    }
  };
  if (existing) {
    applyBadgeState(existing);
    return;
  }
  const badge = document.createElement('span');
  badge.className = 'activity-badge';
  applyBadgeState(badge);
  ticketsBtn.appendChild(badge);
}

async function refreshTicketsBadge() {
  const appName = getCurrentAppName();
  if (!appName) {
    clearTicketsBadge();
    return;
  }

  const seq = ++ticketBadgeReqSeq;
  try {
    const url = `${getDashboardRelativeBase()}/tickets?_=${Date.now()}`;
    const res = await fetch(url, { credentials: 'same-origin' });
    if (!res.ok) throw new Error('Failed to fetch tickets');
    const data = await res.json();
    if (seq !== ticketBadgeReqSeq) return;

    const payload = (data && data.payload && Array.isArray(data.payload)) ? data.payload : [];
    const total = payload
      .filter((ticket) => ticket && ticket.app_name === appName)
      .reduce((sum, ticket) => sum + (Number(ticket.count) || 0), 0);
    upsertTicketsBadge(total);
  } catch (_) {
    if (seq !== ticketBadgeReqSeq) return;
    clearTicketsBadge();
  }
}

const ACTIVITY_BAR_CONFIG = {
  appRequiredActions: ['files', 'databases', 'routes', 'tickets', 'gitlog', 'i18n'],
  actions: [
    {
      id: 'apps',
      title: 'Apps',
      icon: '<i class="fas fa-th-large" aria-hidden="true"></i>',
      tooltip: 'Manage Applications',
      route: function() { return getDashboardBaseUrl() + '/index'; }
    },
    {
      id: 'files',
      title: 'Files',
      icon: '<i class="far fa-file-code" aria-hidden="true"></i>',
      tooltip: 'File Browser',
      route: function() { return buildDashboardViewUrl('files'); }
    },
    {
      id: 'databases',
      title: 'Databases',
      icon: '<i class="fas fa-database" aria-hidden="true"></i>',
      tooltip: 'Database Admin',
      route: function() { return buildDashboardViewUrl('databases'); }
    },
    {
      id: 'routes',
      title: 'Routes',
      icon: '<i class="fas fa-project-diagram" aria-hidden="true"></i>',
      tooltip: 'View Routes',
      route: function() { return buildDashboardViewUrl('routes'); }
    },
    {
      id: 'tickets',
      title: 'Tickets',
      icon: '<i class="fas fa-bug" aria-hidden="true"></i>',
      tooltip: 'Error Tickets',
      route: function() {
        const appName = getCurrentAppName();
        return appName
          ? getDashboardBaseUrl() + '/tickets/search?app_name=' + encodeURIComponent(appName)
          : getDashboardBaseUrl() + '/tickets/search';
      }
    },
    {
      id: 'gitlog',
      title: 'Gitlog',
      icon: '<i class="fas fa-code-branch" aria-hidden="true"></i>',
      tooltip: 'Git Log',
      route: function() { 
        const appName = getCurrentAppName();
        return appName ? getDashboardBaseUrl() + `/gitlog/${appName}` : '#'; 
      }
    },
    {
      id: 'i18n',
      title: 'i18n',
      icon: '<i class="fas fa-language" aria-hidden="true"></i>',
      tooltip: 'Translations',
      route: function() { 
        const appName = getCurrentAppName();
        return appName ? getDashboardBaseUrl() + `/translations/${appName}` : '#'; 
      }
    },
    {
      id: 'settings',
      title: 'Settings',
      icon: '<i class="fas fa-cog" aria-hidden="true"></i>',
      tooltip: 'Dashboard Settings',
      route: function() { return getDashboardBaseUrl() + '/settings'; }
    }
  ],

  bottomActions: [
    {
      id: 'logout',
      title: 'Logout',
      icon: '<i class="fas fa-sign-out-alt" aria-hidden="true"></i>',
      tooltip: 'Logout',
      handler: function() {
        if (window.py4webDashboardApp && typeof window.py4webDashboardApp.logout === 'function') {
          window.py4webDashboardApp.logout();
        }
      }
    }
  ],

  separatorAfter: []
};

function hasSelectedApp() {
  return !!getCurrentAppName();
}

function showSelectAppFirstPage() {
  const shell = document.querySelector('.dashboard-shell');
  if (!shell) {
    return;
  }

  const existing = document.getElementById('select-app-first-page');
  if (existing) {
    return;
  }

  const blocksToHide = shell.querySelectorAll('.dialog-error, .classic-main-layout, .panel');
  blocksToHide.forEach((node) => {
    node.style.display = 'none';
  });

  const message = document.createElement('div');
  message.id = 'select-app-first-page';
  message.className = 'select-app-first-page';
  message.innerHTML = '<h2>Select an Application first</h2>';
  shell.appendChild(message);
}

/**
 * Initialize Activity Bar on page load
 */
function initializeActivityBar() {
  try {
    const activityBar = document.getElementById('activity-bar');
    if (!activityBar) return;

    const activeTheme = document.documentElement.getAttribute('data-theme') || '';
    if (activeTheme !== 'Modern') {
      activityBar.innerHTML = '';
      activityBar.style.display = 'none';
      return;
    }
    activityBar.style.display = '';

    // Remove all existing buttons (in case of re-init)
    activityBar.innerHTML = '';

    const createActivityButton = (action) => {
      const button = document.createElement('button');
      button.className = 'activity-button';
      button.id = `activity-btn-${action.id}`;
      button.title = action.tooltip || action.title;
      button.innerHTML = action.icon;
      button.onclick = function(e) {
        e.preventDefault();
        if (action.id !== 'logout') {
          const actionNeedsApp = ACTIVITY_BAR_CONFIG.appRequiredActions.includes(action.id);
          if (actionNeedsApp && !hasSelectedApp()) {
            return;
          }
          if (action.id === 'apps') {
            window.currentAppName = null;
            localStorage.removeItem('modernTheme_lastApp');
          }
        }
        if (typeof action.handler === 'function') {
          action.handler();
          return;
        }
        let route = '#';
        try {
          route = action.route();
        } catch (_) {
          route = '#';
        }
        if (route && route !== '#') {
          window.location.href = route;
        }
      };
      return button;
    };

    // Add activity buttons
    const appSelected = hasSelectedApp();
    ACTIVITY_BAR_CONFIG.actions.forEach((action) => {
      const actionNeedsApp = ACTIVITY_BAR_CONFIG.appRequiredActions.includes(action.id);
      if (actionNeedsApp && !appSelected) {
        return;
      }

      activityBar.appendChild(createActivityButton(action));

      // Add separator if configured
      if (ACTIVITY_BAR_CONFIG.separatorAfter.includes(action.id)) {
        const separator = document.createElement('div');
        separator.className = 'activity-separator';
        activityBar.appendChild(separator);
      }
    });

    if (ACTIVITY_BAR_CONFIG.bottomActions.length) {
      const spacer = document.createElement('div');
      spacer.className = 'activity-spacer';
      activityBar.appendChild(spacer);
      ACTIVITY_BAR_CONFIG.bottomActions.forEach((action) => {
        const button = createActivityButton(action);
        button.classList.add('activity-button-bottom');
        activityBar.appendChild(button);
      });
    }

    // Set active button based on current route
    updateActiveButton();

    // Store app name for later navigation
    storeCurrentApp();

    // Show app-specific ticket count badge on the Tickets icon.
    refreshTicketsBadge();

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('app_required') === '1') {
      showSelectAppFirstPage();
    }
  } catch (_) {
    // Never let theme script block dashboard functionality.
  }
}

/**
 * Determine current app name from page context
 */
function getCurrentAppName() {
  // Try to get from window variable if available
  if (window.dbAdminAppName) return window.dbAdminAppName;
  if (window.currentAppName) return window.currentAppName;
  
  // Try to extract from URL parameter
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('app')) return urlParams.get('app');
  
  // Try to extract from hash/route
  const pathname = window.location.pathname;
  const match = pathname.match(/api\/(apps|walk|gitlog|translations)\/(\w+)/);
  if (match && match[2]) return match[2];
  
  // Get from localStorage
  return localStorage.getItem('modernTheme_lastApp') || null;
}

/**
 * Store current app name in localStorage for navigation
 */
function storeCurrentApp() {
  const appName = getCurrentAppName();
  if (appName) {
    localStorage.setItem('modernTheme_lastApp', appName);
  }
}

/**
 * Determine which activity button should be active based on current route
 */
function getActiveActionId() {
  const pathname = window.location.pathname;
  const search = new URLSearchParams(window.location.search);

  if (pathname.includes('/index')) {
    const view = search.get('view');
    if (view === 'files' || view === 'routes' || view === 'databases') {
      return view;
    }
  }
  
  // Map routes to action IDs
  const routeMap = {
    '/index': 'apps',
    '/settings': 'settings',
    '/info': 'info',
    '/routes': 'routes',
    '/tickets': 'tickets',
    '/api/tickets': 'tickets',
    '/tickets/search': 'tickets',
    '/dbadmin': 'databases',
    '/walk': 'files',
    '/api/walk': 'files',
    '/gitlog': 'gitlog',
    '/api/gitlog': 'gitlog',
    '/translations': 'i18n',
    '/api/translations': 'i18n',
  };
  
  // Check for exact matches first
  for (const [route, actionId] of Object.entries(routeMap)) {
    if (pathname.includes(route)) {
      return actionId;
    }
  }
  
  // Default to 'apps' if no match
  return 'apps';
}

/**
 * Update active state of Activity buttons
 */
function updateActiveButton() {
  // Remove active class from all buttons
  document.querySelectorAll('.activity-button').forEach(btn => {
    btn.classList.remove('active');
  });
  
  // Add active class to current action
  const activeId = getActiveActionId();
  const activeBtn = document.getElementById(`activity-btn-${activeId}`);
  if (activeBtn) {
    activeBtn.classList.add('active');
  }
}

/**
 * Listen for navigation events to update active button
 */
window.addEventListener('popstate', function() {
  updateActiveButton();
  storeCurrentApp();
  refreshTicketsBadge();
});

/**
 * Initialize Activity Bar when DOM is ready
 */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeActivityBar);
} else {
  initializeActivityBar();
}

/**
 * Re-initialize after Vue/page changes
 */
window.addEventListener('load', function() {
  setTimeout(initializeActivityBar, 250);
  setTimeout(initializeActivityBar, 1000);
});

// Export for external use
window.ModernTheme = {
  initializeActivityBar: initializeActivityBar,
  updateActiveButton: updateActiveButton,
  getCurrentAppName: getCurrentAppName,
  refreshTicketsBadge: refreshTicketsBadge
};

    /**
     * Modern App Browser — tabbed panel (Files, Databases, Routes)
     * Replaces accordion views for the Modern theme.
     * Files tab: split-pane folder tree + ACE editor.
     * Databases tab: clickable table list → dbadmin.
     * Routes tab: sortable routes table + reload.
     */
    (() => {
      const getAppBase = () => {
        const parts = window.location.pathname.split('/').filter(Boolean);
        return parts.length ? '/' + parts[0] : '';
      };

      const encodePath = (path) => path.split('/').map(encodeURIComponent).join('/');

      let mfbAceEditor = null;
      let mfbCurrentFilePath = null;
      let mfbSelectedFileEl = null;
      let mfbSelectedFolderEl = null;
      let mfbCurrentApp = null;
      let mfbDirtyState = { lastLoadedText: '', suppress: false };

      // ---------- Dialogs ----------
      const showMfbDialog = (title, body, buttons) => {
        return new Promise((resolve) => {
          const overlay = document.createElement('div');
          overlay.className = 'modern-fb-dialog-overlay';
          const btnsHtml = buttons
            .map((b, i) => `<button class="modern-fb-dialog-btn" data-idx="${i}" ${b.primary ? '' : 'style="background:var(--bg-tertiary);color:var(--text-primary);border:1px solid var(--border-color);"'}>${b.label}</button>`)
            .join('');
          overlay.innerHTML = `
            <div class="modern-fb-dialog">
              <div class="modern-fb-dialog-header"><h3>${title}</h3></div>
              <div class="modern-fb-dialog-body">${body}</div>
              <div class="modern-fb-dialog-footer">${btnsHtml}</div>
            </div>`;
          document.body.appendChild(overlay);
          overlay.querySelectorAll('.modern-fb-dialog-btn').forEach((btn) => {
            btn.addEventListener('click', () => {
              const inputEl = overlay.querySelector('#mfb-prompt-input');
              const inputValue = inputEl ? inputEl.value.trim() : null;
              const idx = parseInt(btn.dataset.idx, 10);
              overlay.remove();
              resolve({ idx, inputValue });
            });
          });
        });
      };

      const confirmDialog = (title, message) =>
        showMfbDialog(title, `<p>${message}</p>`, [
          { label: 'Confirm', primary: true },
          { label: 'Cancel', primary: false },
        ]).then((result) => result.idx === 0);

      const promptDialog = (title, label, placeholder) =>
        showMfbDialog(
          title,
          `<p>${label}</p><input type="text" id="mfb-prompt-input" placeholder="${placeholder}" style="width:100%;margin-top:8px;" />`,
          [{ label: 'OK', primary: true }, { label: 'Cancel', primary: false }]
        ).then((result) => {
          if (result.idx !== 0) return null;
          return result.inputValue || null;
        });

      // ---------- Dirty state ----------
      const isDirty = () => mfbAceEditor && mfbAceEditor.getValue() !== mfbDirtyState.lastLoadedText;

      const setDirtyUi = (dirty) => {
        const saveBtn = document.getElementById('mfb-btn-save');
        if (!saveBtn) return;
        saveBtn.classList.toggle('modern-fb-dirty-indicator', Boolean(dirty) && !saveBtn.disabled);
      };

      const confirmIfDirty = async () => {
        if (!isDirty()) return true;
        return confirmDialog('Unsaved Changes', 'You have unsaved changes. Proceed and lose them?');
      };

      // ---------- ACE editor ----------
      const initAce = () => {
        const el = document.getElementById('modern-ace-editor');
        if (!el) return;
        if (mfbAceEditor) { try { mfbAceEditor.destroy(); } catch (_) {} mfbAceEditor = null; }
        mfbAceEditor = ace.edit(el);
        mfbAceEditor.setTheme('ace/theme/chrome');
        mfbAceEditor.setOptions({ fontSize: '13px', showPrintMargin: false, wrap: true });
        mfbDirtyState = { lastLoadedText: '', suppress: false };
        mfbAceEditor.session.on('change', () => {
          if (mfbDirtyState.suppress) return;
          setDirtyUi(mfbAceEditor.getValue() !== mfbDirtyState.lastLoadedText);
        });
      };

      // ---------- Folder tree builder ----------
      const buildFolderTree = (sections, appName) => {
        const hierarchy = { '': [] };
        Object.keys(sections).forEach((section) => {
          if (!section) return;
          const parts = section.split('/');
          const parent = parts.length === 1 ? '' : parts.slice(0, -1).join('/');
          if (!hierarchy[parent]) hierarchy[parent] = [];
          hierarchy[parent].push(section);
        });

        const createNode = (folderPath, isRoot) => {
          const folderName = folderPath.split('/').pop() || appName;
          const files = sections[folderPath] || [];
          const children = hierarchy[folderPath] || [];
          if (isRoot) {
            let html = `<ul class="modern-fb-folder-list modern-fb-root-list" data-mfb-folder-list="${folderPath}">`;
            files.forEach((f) => { html += `<li><button class="modern-fb-file-btn" data-mfb-file data-mfb-section="${folderPath}" data-mfb-filename="${f}">${f}</button></li>`; });
            children.forEach((c) => { html += createNode(c, false); });
            html += '</ul>';
            return html;
          }
          let html = `<li class="modern-fb-subfolder">
            <button class="modern-fb-folder-toggle" data-mfb-folder="${folderPath}">
              <span class="modern-fb-folder-arrow">▶</span><i class="fas fa-folder"></i> ${folderName}
            </button>
            <div class="modern-fb-folder-children" data-mfb-children="${folderPath}">
              <ul class="modern-fb-folder-list" data-mfb-folder-list="${folderPath}">`;
          files.forEach((f) => { html += `<li><button class="modern-fb-file-btn" data-mfb-file data-mfb-section="${folderPath}" data-mfb-filename="${f}">${f}</button></li>`; });
          children.forEach((c) => { html += createNode(c, false); });
          html += `</ul></div></li>`;
          return html;
        };

        const hasAny = (sections['']?.length || 0) + (hierarchy['']?.length || 0);
        if (!hasAny) return '<div style="padding:12px;color:var(--text-secondary)">No files found.</div>';
        return `<div class="modern-fb-folder-root">
          <button class="modern-fb-folder-toggle open" data-mfb-folder="">
            <span class="modern-fb-folder-arrow">▶</span><i class="fas fa-folder-open"></i> ${appName}
          </button>
          <div class="modern-fb-folder-children open" data-mfb-children="">${createNode('', true)}</div>
        </div>`;
      };

      // ---------- Body HTML per view ----------
      const renderFilesBodyHtml = (payload) => `
        <div class="modern-fb-left">
          <div class="modern-fb-tree" id="mfb-tree">
            ${buildFolderTree(payload.sections || {}, payload.name)}
          </div>
        </div>
        <div class="modern-fb-right">
          <div class="modern-fb-editor-wrap"><div id="modern-ace-editor"></div></div>
          <div class="modern-fb-status" id="mfb-status">Select a file to edit</div>
          <div class="modern-fb-actions">
            <button id="mfb-btn-save" disabled><i class="fas fa-save"></i> Save File</button>
            <button id="mfb-btn-reload" disabled><i class="fas fa-sync-alt"></i> Reload</button>
            <button id="mfb-btn-delete" class="btn-danger" disabled><i class="fas fa-trash"></i> Delete</button>
            <button id="mfb-btn-add-file"><i class="fas fa-plus"></i> Add File</button>
            <button id="mfb-btn-add-folder"><i class="fas fa-folder-plus"></i> Add Folder</button>
            <button id="mfb-btn-upload"><i class="fas fa-upload"></i> Upload New File</button>
          </div>
        </div>`;

      const renderDatabasesBodyHtml = (appName) => `
        <div class="modern-fb-full-content">
          <div class="modern-fb-section-header">
            <h3>Databases for ${appName}</h3>
            <button id="mfb-btn-db-reload"><i class="fas fa-sync-alt"></i> Reload</button>
          </div>
          <div id="mfb-db-container"><p>Loading…</p></div>
        </div>`;

      const renderRoutesBodyHtml = (appName) => `
        <div class="modern-fb-full-content">
          <div class="modern-fb-section-header">
            <h3>Routes for ${appName}</h3>
            <div style="display:flex;gap:8px;">
              <button id="mfb-btn-routes-reload"><i class="fas fa-sync-alt"></i> Reload Routes</button>
            </div>
          </div>
          <div id="mfb-routes-container"><p>Loading…</p></div>
        </div>`;

      const renderMfbBodyHtml = (payload, view) => {
        if (view === 'databases') return renderDatabasesBodyHtml(payload.name);
        if (view === 'routes') return renderRoutesBodyHtml(payload.name);
        return renderFilesBodyHtml(payload);
      };

      // ---------- Main browser renderer ----------
      const renderModernBrowser = (payload, view = 'files') => {
        mfbCurrentApp = payload;
        const container = document.getElementById('modern-file-browser');
        if (!container) return;

        container.innerHTML = `
          <div class="modern-fb-header">
            <div class="modern-fb-title-row">
              <h2 class="modern-fb-app-name">Edit: ${payload.name}</h2>
              <button class="modern-fb-back-btn" id="mfb-btn-back">
                <i class="fas fa-arrow-left"></i> Back
              </button>
            </div>
          </div>
          <div class="modern-fb-body view-${view}" id="mfb-body">
            ${renderMfbBodyHtml(payload, view)}
          </div>`;

        container.style.display = 'flex';

        // Back button
        document.getElementById('mfb-btn-back')?.addEventListener('click', async () => {
          const body = document.getElementById('mfb-body');
          const currentView = body ? (body.dataset.mfbView || 'files') : 'files';
          if (currentView === 'files') {
            const proceed = await confirmIfDirty();
            if (!proceed) return;
          }
          container.style.display = 'none';
          const appPanel = document.querySelector('.modern-main-layout');
          if (appPanel) appPanel.style.display = '';
          mfbCurrentFilePath = null;
          mfbCurrentApp = null;
          mfbSelectedFileEl = null;
        });

        initMfbView(view);
      };

      const switchMfbView = (newView) => {
        const body = document.getElementById('mfb-body');
        if (!body || !mfbCurrentApp) return;
        body.className = `modern-fb-body view-${newView}`;
        body.dataset.mfbView = newView;
        body.innerHTML = renderMfbBodyHtml(mfbCurrentApp, newView);
        initMfbView(newView);
      };

      const initMfbView = (view) => {
        if (view === 'files') {
          initAce();
          const treeEl = document.getElementById('mfb-tree');
          if (treeEl) bindMfbTreeEvents(treeEl);
          setupMfbFileActionEvents(mfbCurrentApp);
          // Auto-open __init__.py or first file
          const sections = mfbCurrentApp.sections || {};
          const rootFiles = sections[''] || [];
          const autoFile = rootFiles.includes('__init__.py') ? '__init__.py' : rootFiles[0];
          if (autoFile) loadMfbFile('', autoFile).then(() => highlightMfbFile('', autoFile));
        } else if (view === 'databases') {
          loadMfbDatabases(mfbCurrentApp.name);
          document.getElementById('mfb-btn-db-reload')?.addEventListener('click', () => loadMfbDatabases(mfbCurrentApp.name));
        } else if (view === 'routes') {
          loadMfbRoutes(mfbCurrentApp.name);
          document.getElementById('mfb-btn-routes-reload')?.addEventListener('click', () => reloadMfbRoutes(mfbCurrentApp.name));
        }
      };

      // ---------- File operations ----------
      const setStatus = (msg) => { const el = document.getElementById('mfb-status'); if (el) el.textContent = msg; };

      const setBtnsForFile = (enabled) => {
        ['mfb-btn-save', 'mfb-btn-reload', 'mfb-btn-delete'].forEach((id) => {
          const btn = document.getElementById(id);
          if (btn) btn.disabled = !enabled;
        });
        if (!enabled) setDirtyUi(false);
      };

      const setBtnsForFolder = (enabled) => {
        const saveBtn = document.getElementById('mfb-btn-save');
        const reloadBtn = document.getElementById('mfb-btn-reload');
        const deleteBtn = document.getElementById('mfb-btn-delete');
        if (saveBtn) saveBtn.disabled = true;
        if (reloadBtn) reloadBtn.disabled = true;
        if (deleteBtn) deleteBtn.disabled = !enabled;
        setDirtyUi(false);
      };

      const clearEditorForFolderSelection = () => {
        if (!mfbAceEditor) return;
        mfbDirtyState.suppress = true;
        mfbAceEditor.setValue('', -1);
        mfbDirtyState.lastLoadedText = '';
        mfbDirtyState.suppress = false;
        setDirtyUi(false);
      };

      const loadMfbFile = async (section, filename) => {
        if (!mfbCurrentApp) return;
        const appBase = getAppBase();
        const filePath = section ? `${mfbCurrentApp.name}/${section}/${filename}` : `${mfbCurrentApp.name}/${filename}`;
        mfbCurrentFilePath = filePath;
        if (mfbSelectedFolderEl) {
          mfbSelectedFolderEl.classList.remove('selected-folder');
          mfbSelectedFolderEl = null;
        }
        setBtnsForFile(false);
        setStatus(`Loading ${filePath}…`);
        try {
          const res = await fetch(`${appBase}/load/${encodePath(filePath)}`);
          if (!res.ok) throw new Error('Load failed');
          const data = await res.json();
          if (mfbAceEditor) {
            const modelist = ace.require('ace/ext/modelist');
            mfbAceEditor.session.setMode(modelist.getModeForPath(filePath).mode);
            mfbDirtyState.suppress = true;
            mfbDirtyState.lastLoadedText = data.payload || '';
            mfbAceEditor.setValue(mfbDirtyState.lastLoadedText, -1);
            mfbDirtyState.suppress = false;
            setDirtyUi(false);
          }
          setBtnsForFile(true);
          setStatus(filePath);
        } catch (err) {
          setStatus(`Error: ${err.message}`);
        }
      };

      const saveMfbFile = async () => {
        if (!mfbCurrentFilePath || !mfbAceEditor) return;
        const appBase = getAppBase();
        setStatus(`Saving ${mfbCurrentFilePath}…`);
        try {
          const res = await fetch(`${appBase}/save/${encodePath(mfbCurrentFilePath)}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(mfbAceEditor.getValue()),
          });
          if (!res.ok) throw new Error('Save failed');
          const data = await res.json();
          if (data.status !== 'success') throw new Error(data.message || 'Save failed');
          mfbDirtyState.lastLoadedText = mfbAceEditor.getValue();
          setDirtyUi(false);
          setStatus(`Saved ${mfbCurrentFilePath}`);
        } catch (err) {
          setStatus(`Error: ${err.message}`);
        }
      };

      const refreshMfbTree = async (reopenPath) => {
        if (!mfbCurrentApp) return;
        const appBase = getAppBase();
        try {
          const res = await fetch(`${appBase}/app_detail/${encodeURIComponent(mfbCurrentApp.name)}`);
          if (!res.ok) throw new Error('Refresh failed');
          const data = await res.json();
          if (data.status !== 'success') throw new Error(data.message || 'Refresh failed');
          mfbCurrentApp = data.payload;
          const treeEl = document.getElementById('mfb-tree');
          if (treeEl) {
            treeEl.innerHTML = buildFolderTree(mfbCurrentApp.sections || {}, mfbCurrentApp.name);
            bindMfbTreeEvents(treeEl);
          }
          if (reopenPath) {
            const parts = reopenPath.split('/');
            const filename = parts.pop();
            const section = parts.slice(1).join('/');
            await loadMfbFile(section, filename);
            highlightMfbFile(section, filename);
          }
        } catch (err) {
          setStatus(`Refresh error: ${err.message}`);
        }
      };

      const highlightMfbFile = (section, filename) => {
        if (mfbSelectedFolderEl) {
          mfbSelectedFolderEl.classList.remove('selected-folder');
          mfbSelectedFolderEl = null;
        }
        if (mfbSelectedFileEl) mfbSelectedFileEl.classList.remove('selected-file');
        const btn = document.querySelector(`[data-mfb-file][data-mfb-section="${section}"][data-mfb-filename="${filename}"]`);
        if (btn) {
          btn.classList.add('selected-file');
          mfbSelectedFileEl = btn;
          const childrenEl = btn.closest('.modern-fb-folder-children');
          if (childrenEl && !childrenEl.classList.contains('open')) {
            childrenEl.classList.add('open');
            const toggleBtn = document.querySelector(`[data-mfb-folder="${childrenEl.dataset.mfbChildren}"]`);
            if (toggleBtn) toggleBtn.classList.add('open');
          }
        }
      };

      // ---------- Tree events ----------
      const bindMfbTreeEvents = (root) => {
        root.querySelectorAll('[data-mfb-folder]').forEach((btn) => {
          btn.addEventListener('click', () => {
            const folderPath = btn.dataset.mfbFolder;
            const childrenEl = document.querySelector(`[data-mfb-children="${folderPath}"]`);
            if (!childrenEl) return;
            const open = childrenEl.classList.toggle('open');
            btn.classList.toggle('open', open);

            // Select non-root folders so empty directories can be deleted.
            if (folderPath) {
              if (mfbSelectedFileEl) {
                mfbSelectedFileEl.classList.remove('selected-file');
                mfbSelectedFileEl = null;
              }
              if (mfbSelectedFolderEl && mfbSelectedFolderEl !== btn) {
                mfbSelectedFolderEl.classList.remove('selected-folder');
              }
              mfbSelectedFolderEl = btn;
              btn.classList.add('selected-folder');
              mfbCurrentFilePath = `${mfbCurrentApp.name}/${folderPath}`;
              clearEditorForFolderSelection();
              setBtnsForFolder(true);
              setStatus(mfbCurrentFilePath);
            }
          });
        });
        root.querySelectorAll('[data-mfb-file]').forEach((btn) => {
          btn.addEventListener('click', async () => {
            const proceed = await confirmIfDirty();
            if (!proceed) return;
            if (mfbSelectedFolderEl) {
              mfbSelectedFolderEl.classList.remove('selected-folder');
              mfbSelectedFolderEl = null;
            }
            if (mfbSelectedFileEl) mfbSelectedFileEl.classList.remove('selected-file');
            btn.classList.add('selected-file');
            mfbSelectedFileEl = btn;
            await loadMfbFile(btn.dataset.mfbSection, btn.dataset.mfbFilename);
          });
        });
      };

      // ---------- File action buttons ----------
      const setupMfbFileActionEvents = (payload) => {
        document.getElementById('mfb-btn-save')?.addEventListener('click', saveMfbFile);

        document.getElementById('mfb-btn-reload')?.addEventListener('click', async () => {
          if (!mfbCurrentFilePath) return;
          const proceed = await confirmIfDirty();
          if (!proceed) return;
          const parts = mfbCurrentFilePath.split('/');
          const filename = parts.pop();
          const section = parts.slice(1).join('/');
          await loadMfbFile(section, filename);
        });

        document.getElementById('mfb-btn-delete')?.addEventListener('click', async () => {
          if (!mfbCurrentFilePath) return;
          const ok = await confirmDialog('Delete Item', `Delete "${mfbCurrentFilePath}"? This cannot be undone.`);
          if (!ok) return;
          const appBase = getAppBase();
          setStatus(`Deleting ${mfbCurrentFilePath}…`);
          try {
            const res = await fetch(`${appBase}/delete/${encodePath(mfbCurrentFilePath)}`, { method: 'POST' });
            if (!res.ok) throw new Error('Delete failed');
            const data = await res.json();
            if (data.status !== 'success') throw new Error(data.message || 'Delete failed');
            setBtnsForFile(false);
            if (mfbAceEditor) {
              mfbDirtyState.suppress = true; mfbAceEditor.setValue('', -1); mfbDirtyState.lastLoadedText = ''; mfbDirtyState.suppress = false;
            }
            if (mfbSelectedFileEl) {
              mfbSelectedFileEl.classList.remove('selected-file');
              mfbSelectedFileEl = null;
            }
            if (mfbSelectedFolderEl) {
              mfbSelectedFolderEl.classList.remove('selected-folder');
              mfbSelectedFolderEl = null;
            }
            mfbCurrentFilePath = null;
            setStatus('Item deleted.');
            await refreshMfbTree(null);
          } catch (err) { setStatus(`Error: ${err.message}`); }
        });

        document.getElementById('mfb-btn-add-file')?.addEventListener('click', async () => {
          const name = await promptDialog('Add File', 'Enter the new file name (relative path allowed):', 'e.g. controllers.py or static/js/app.js');
          if (!name) return;
          const appBase = getAppBase();
          const filePath = `${payload.name}/${name}`;
          setStatus(`Creating ${filePath}…`);
          try {
            const res = await fetch(`${appBase}/new_file/${encodePath(filePath)}`, { method: 'POST' });
            if (!res.ok) throw new Error('Create failed');
            const data = await res.json();
            if (data.status !== 'success') throw new Error(data.message || 'Create failed');
            setStatus(`Created ${filePath}`);
            await refreshMfbTree(null);
            const parts = name.split('/');
            const filename = parts.pop();
            const section = parts.join('/');
            await loadMfbFile(section, filename);
            highlightMfbFile(section, filename);
          } catch (err) { setStatus(`Error: ${err.message}`); }
        });

        document.getElementById('mfb-btn-add-folder')?.addEventListener('click', async () => {
          const name = await promptDialog('Add Folder', 'Enter the new folder name:', 'e.g. utils');
          if (!name) return;
          const appBase = getAppBase();
          const folderPath = `${payload.name}/${name}`;
          setStatus(`Creating folder ${name}…`);
          try {
            const res = await fetch(`${appBase}/new_file/${encodePath(folderPath)}?folder=1`, { method: 'POST' });
            if (!res.ok) throw new Error('Create failed');
            const data = await res.json();
            if (data.status !== 'success') throw new Error(data.message || 'Create failed');
            setStatus(`Created folder ${name}`);
            await refreshMfbTree(null);
          } catch (err) { setStatus(`Error: ${err.message}`); }
        });

        document.getElementById('mfb-btn-upload')?.addEventListener('click', () => {
          const dashboardApp = window.py4webDashboardApp;
          if (!dashboardApp || typeof dashboardApp.upload_new_file !== 'function') {
            setStatus('Error: Upload action is not available.'); return;
          }
          dashboardApp.selected_app = { name: payload.name };
          dashboardApp.selected_folder = mfbCurrentFilePath
            ? `${payload.name}/${mfbCurrentFilePath.split('/').slice(1, -1).join('/')}`
            : null;
          dashboardApp.upload_new_file();
          const pollRefresh = setInterval(() => {
            if (!dashboardApp.modal) { clearInterval(pollRefresh); refreshMfbTree(null); }
          }, 400);
        });
      };

      // ---------- Databases view ----------
      const loadMfbDatabases = async (appName) => {
        const container = document.getElementById('mfb-db-container');
        if (!container) return;
        const appBase = getAppBase();
        container.innerHTML = '<p>Loading…</p>';
        try {
          const res = await fetch(`${appBase}/rest/${encodeURIComponent(appName)}`);
          const data = await res.json();
          if (data.status === 'success' && data.databases) {
            const allTables = [];
            (data.databases || []).forEach((db) => {
              (db.tables || []).forEach((table) => {
                allTables.push({ dbName: db.name, tableName: table.name, fields: table.fields || [] });
              });
            });
            if (allTables.length === 0) {
              container.innerHTML = '<p>No tables found in databases.</p>';
              return;
            }
            container.innerHTML = `<div class="modern-fb-db-list">
              ${allTables.map((t) => `
                <div class="modern-fb-db-row" data-db="${t.dbName}" data-table="${t.tableName}">
                  <span class="modern-fb-db-name"><i class="fas fa-table"></i> ${t.dbName}.${t.tableName}</span>
                  <span class="modern-fb-db-fields">${t.fields.join(', ')}</span>
                  <span class="modern-fb-db-arrow">→</span>
                </div>`).join('')}
            </div>`;
            container.querySelectorAll('.modern-fb-db-row').forEach((row) => {
              row.addEventListener('click', () => {
                window.location.href = `${appBase}/dbadmin/${encodeURIComponent(appName)}/${encodeURIComponent(row.dataset.db)}/${encodeURIComponent(row.dataset.table)}`;
              });
            });
          } else {
            container.innerHTML = '<p>Could not load databases.</p>';
          }
        } catch (err) {
          container.innerHTML = `<p>Error: ${err.message}</p>`;
        }
      };

      // ---------- Routes view ----------
      const loadMfbRoutes = async (appName) => {
        const container = document.getElementById('mfb-routes-container');
        if (!container) return;
        const appBase = getAppBase();
        container.innerHTML = '<p>Loading…</p>';
        try {
          const res = await fetch(`${appBase}/routes`);
          const data = await res.json();
          if (data.status === 'success' && data.payload) {
            const routes = data.payload[appName] || [];
            if (routes.length === 0) { container.innerHTML = '<p>No routes found for this app.</p>'; return; }

            const sortState = { key: 'rule', dir: 'asc' };
            const metricKeys = new Set(['time', 'calls', 'errors']);
            const fmt = (v) => { const n = Number(v); return Number.isFinite(n) ? n.toFixed(2) : '0.00'; };
            const sorted = () => {
              const dir = sortState.dir === 'asc' ? 1 : -1;
              return [...routes].sort((a, b) => {
                let av = a[sortState.key], bv = b[sortState.key];
                if (metricKeys.has(sortState.key)) { av = Number(av || 0); bv = Number(bv || 0); }
                else { av = String(av || '').toLowerCase(); bv = String(bv || '').toLowerCase(); }
                return av < bv ? -dir : av > bv ? dir : 0;
              });
            };
            const mark = (k) => sortState.key === k ? (sortState.dir === 'asc' ? ' ▲' : ' ▼') : '';
            const thStyle = 'padding:8px;border:1px solid var(--border-color);text-align:left;cursor:pointer;background:var(--bg-tertiary);color:var(--text-primary);';
            const tdStyle = 'padding:6px 8px;border:1px solid var(--border-color);color:var(--text-primary);';

            const renderTable = () => {
              container.innerHTML = `<div class="modern-fb-routes-scroll">
                <table style="width:100%;border-collapse:collapse;">
                  <thead><tr>
                    ${['rule','method','filename','action','time','calls','errors'].map((k) =>
                      `<th data-sk="${k}" style="${thStyle}">${k.charAt(0).toUpperCase()+k.slice(1)}${mark(k)}</th>`
                    ).join('')}
                  </tr></thead>
                  <tbody>${sorted().map((r) => `<tr>
                    <td style="${tdStyle}"><a href="${r.rule}" target="_blank" style="color:var(--accent-secondary)"><code>${r.rule}</code></a></td>
                    <td style="${tdStyle}"><code>${r.method}</code></td>
                    <td style="${tdStyle}"><code>${r.filename || ''}</code></td>
                    <td style="${tdStyle}"><code>${r.action}</code></td>
                    <td style="${tdStyle}"><code>${fmt(r.time)}</code></td>
                    <td style="${tdStyle}"><code>${fmt(r.calls)}</code></td>
                    <td style="${tdStyle}"><code>${fmt(r.errors)}</code></td>
                  </tr>`).join('')}</tbody>
                </table>
              </div>`;
              container.querySelectorAll('th[data-sk]').forEach((th) => {
                th.addEventListener('click', () => {
                  const k = th.dataset.sk;
                  if (sortState.key === k) sortState.dir = sortState.dir === 'asc' ? 'desc' : 'asc';
                  else { sortState.key = k; sortState.dir = metricKeys.has(k) ? 'desc' : 'asc'; }
                  renderTable();
                });
              });
            };
            renderTable();
          } else {
            container.innerHTML = '<p>Could not load routes.</p>';
          }
        } catch (err) {
          container.innerHTML = `<p>Error: ${err.message}</p>`;
        }
      };

      const reloadMfbRoutes = async (appName) => {
        const btn = document.getElementById('mfb-btn-routes-reload');
        if (btn) btn.disabled = true;
        const appBase = getAppBase();
        try {
          await fetch(`${appBase}/reload/${encodeURIComponent(appName)}`);
          await loadMfbRoutes(appName);
        } catch (err) {
          const c = document.getElementById('mfb-routes-container');
          if (c) c.innerHTML = `<p>Error: ${err.message}</p>`;
        } finally {
          if (btn) btn.disabled = false;
        }
      };

      // ---------- Entry point ----------
      const modernHandleEdit = async (appName, view = 'files') => {
        const appBase = getAppBase();
        const appPanel = document.querySelector('.modern-main-layout');
        const container = document.getElementById('modern-file-browser');
        if (!container) return;

        // Store app name so activity bar shows app-required buttons (Files/DB/Routes/Tickets)
        window.currentAppName = appName;
        localStorage.setItem('modernTheme_lastApp', appName);
        initializeActivityBar();
        refreshTicketsBadge();

        if (appPanel) appPanel.style.display = 'none';
        container.style.display = 'flex';
        container.innerHTML = `<div class="modern-fb-loading"><i class="fas fa-spinner fa-spin"></i>&nbsp; Loading ${appName}…</div>`;

        // Databases and Routes don't need app_detail (no file tree needed)
        if (view === 'databases' || view === 'routes') {
          const fakePayload = { name: appName, sections: {} };
          renderModernBrowser(fakePayload, view);
          return;
        }

        try {
          const res = await fetch(`${appBase}/app_detail/${encodeURIComponent(appName)}`);
          if (!res.ok) throw new Error('Failed to load app detail');
          const data = await res.json();
          if (data.status !== 'success') throw new Error(data.message || 'Error loading app detail');
          renderModernBrowser(data.payload, view);
        } catch (err) {
          container.innerHTML = `<div class="modern-fb-loading" style="color:#e74c3c;">Error: ${err.message}</div>`;
          if (appPanel) appPanel.style.display = '';
        }
      };

      // ---------- Auto-trigger on URL params ----------
      const maybeAutoTrigger = () => {
        try {
          const activeTheme = document.documentElement.getAttribute('data-theme') || '';
          if (activeTheme !== 'Modern') return;
          const params = new URLSearchParams(window.location.search);
          const view = params.get('view');
          if (!['files', 'databases', 'routes'].includes(view)) return;
          const appName = params.get('app') || localStorage.getItem('modernTheme_lastApp');
          if (!appName) return;
          modernHandleEdit(appName, view);
        } catch (_) {}
      };

      // Register hook for index.js handleEdit() — always opens Files tab
      window.classicEditHandler = (appName) => modernHandleEdit(appName, 'files');

      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => setTimeout(maybeAutoTrigger, 350));
      } else {
        setTimeout(maybeAutoTrigger, 350);
      }
      window.addEventListener('load', () => setTimeout(maybeAutoTrigger, 800));
    })();

