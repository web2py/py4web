let
  nixpkgs-src = builtins.fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/tarball/nixos-22.11";
  };

  pkgs = import nixpkgs-src {
    config = {
      allowUnfree = true;
    };
  };

  # This is the Python version that will be used.
  myPython = pkgs.python310;

  pythonWithPkgs = myPython.withPackages (pythonPkgs: with pythonPkgs; [
    pip
    setuptools
    wheel
  ]);

  lib-path = with pkgs; lib.makeLibraryPath [
    libffi
    openssl
  ];

  shell = pkgs.mkShell {
    buildInputs = [
      # my python and packages
      pythonWithPkgs
      pkgs.memcached

      # other packages needed for compiling python libs
      pkgs.readline
      pkgs.libffi
      pkgs.openssl
    ];

    shellHook = ''
      # Allow the use of wheels.
      SOURCE_DATE_EPOCH=$(date +%s)

      # Augment the dynamic linker path
      export "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${lib-path}"

      # Setup the virtual environment if it doesn't already exist.
      if test ! -d .venv; then
        python -m venv .venv
      fi
      .venv/bin/pip install -U -r requirements.txt
      source .venv/bin/activate
      export PYTHONPATH=`pwd`.venv/${myPython.sitePackages}/:$PYTHONPATH      
    '';
  };
in

shell