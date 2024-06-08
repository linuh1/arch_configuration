- Install apps:
```sh
pacman -S python-poetry bluez bluez-utils mesa xf86-video-amdgpu vulkan-radeon kitty pipewire ranger zsh wget go git wofi fakeroot waybar flatpak htop syncthing gnu-free-fonts noto-fonts otf-font-awesome ttf-jetbrains-mono-nerd ttf-jetbrains-mono dunst xdg-desktop-portal-hyprland hyprlock mpv wl-clipboard neovim imv grim wf-recorder hyprpaper gammastep networkmanager; flatpak install flathub org.telegram.desktop org.mozilla.firefox md.obsidian.Obsidian com.jetbrains.PyCharm-Community com.discordapp.Discord org.qbittorrent.qBittorrent org.onlyoffice.desktopeditors com.github.tchx84.Flatseal
```

- Add the `exec Hyprland` to the end of the **/etc/profile** file for autostart hyprland after login in tty.

- Add the directory `getty@tty1.service.d` to **/etc/systemd/system/**.

- Add the file `autologin.conf` to the **/etc/systemd/system/getty@tty1.service.d/** directory containing
```
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin danimir tty1
```
for autologin in tty1.

- Add the `--system-title-bar` flag in the **/var/lib/flatpak/app/org.onlyoffice.desktopeditors/current/active/export/share/applications/org.onlyoffice.desktopeditors.desktop** in the `Exec` section.

- Install oh-my-zsh by this command:
```sh
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

- Enable bluetooth:
```sh
systemctl enable bluetooth.service; systemctl start bluetooth.service
```

- Enable syncthing:
```sh
syncthing; systemctl enable syncthing@danimir.service; systemctl start syncthing@danimir.service
```

- Adding links to the neovim (needed by ranger and git):
```sh
ln -s /bin/nvim /bin/vi; ln -s /bin/nvim /bin/vim
```

- I have not choose bluetooth menu yet. Here are favorites: Bluedevil, Blueman.

- For popup windows for switching keyboard layout, changing volume or brightness I may use dunst scripts or wofi.

- For internet menu need wofi script.

- Start and enable network manager by:
```sh
systemctl enable NetworkManager
systemctl start NetworkManager
```

- To add keyboard layout ru past this in `hyprland.conf`:
```sh
input {
    kb_layout = us,ru
    kb_options = grp:caps_toggle
```
