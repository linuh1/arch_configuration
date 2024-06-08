Install apps:
```sh
pacman -S bluez bluez-utils mesa xf86-video-amdgpu vulkan-radeon kitty pipewire ranger zsh wget go git wofi fakeroot waybar flatpak htop syncthing gnu-free-fonts noto-fonts otf-font-awesome ttf-jetbrains-mono-nerd ttf-jetbrains-mono dunst xdg-desktop-portal-hyprland hyprlock mpv wl-clipboard; flatpak install flathub org.telegram.desktop org.mozilla.firefox md.obsidian.Obsidian com.jetbrains.PyCharm-Community com.discordapp.Discord org.qbittorrent.qBittorrent org.onlyoffice.desktopeditors com.github.tchx84.Flatseal
```

Add the `exec Hyprland` to the end of the **/etc/profile** file for autostart hyprland after login in tty.

Add the directory `getty@tty1.service.d` to **/etc/systemd/system/**.

Add the file `autologin.conf` to the **/etc/systemd/system/getty@tty1.service.d/** directory containing
```
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin danimir tty1
```
for autologin in tty1.

Add the `--system-title-bar` flag in the **/var/lib/flatpak/app/org.onlyoffice.desktopeditors/current/active/export/share/applications/org.onlyoffice.desktopeditors.desktop** in the `Exec` section.
