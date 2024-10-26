let
  nixpkgs-src = builtins.fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/tarball/nixos-23.05";
  };

  pkgs = import nixpkgs-src {};

  # This is the Python version that will be used.
  myPython = pkgs.python311;

  pythonWithPkgs = myPython.withPackages (pythonPkgs: with pythonPkgs; [
    pip
    setuptools
    wheel
    twine
    black
    isort
    pytest
  ]);

  lib-path = with pkgs; lib.makeLibraryPath [
    libffi
    openssl
  ];

  shell = pkgs.mkShell {
    buildInputs = [
      pythonWithPkgs
      pkgs.zip
      pkgs.memcached
      pkgs.redis
      pkgs.readline
      pkgs.libffi
      pkgs.openssl
      pkgs.cmake
    ];

    shellHook = ''
      # Allow the use of wheels.
      SOURCE_DATE_EPOCH=$(date +%s)
      VENV_PATH=/home/$USER/.venvs$(pwd)/venv${myPython.version}
      # Augment the dynamic linker path
      export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${lib-path}"

      # Setup the virtual environment if it doesn't already exist.
      if test ! -d $VENV_PATH; then
        python -m venv $VENV_PATH
      fi
      $VENV_PATH/bin/pip install -U -r requirements.txt
      source $VENV_PATH/bin/activate
      export LOCALE_ARCHIVE=/usr/lib/locale/locale-archive
      export PYTHONPATH=$VENV_PATH/${myPython.sitePackages}/:$PYTHONPATH      
    '';
  };
in

shell