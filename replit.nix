{ pkgs }: {
  deps = [
    pkgs.python38Packages.pip
    pkgs.python38Full
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server
  ];
}