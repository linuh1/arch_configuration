Для настройки системы требуется выполнить ниже описанные действия.

- Установить программы:
```sh
pacman -S python-poetry bluez bluez-utils mesa xf86-video-amdgpu vulkan-radeon kitty pipewire ranger zsh wget go git wofi fakeroot waybar flatpak htop syncthing gnu-free-fonts noto-fonts otf-font-awesome ttf-jetbrains-mono-nerd ttf-jetbrains-mono dunst xdg-desktop-portal-hyprland hyprlock mpv wl-clipboard neovim imv grim wf-recorder hyprpaper gammastep networkmanager; flatpak install flathub org.telegram.desktop org.mozilla.firefox md.obsidian.Obsidian com.jetbrains.PyCharm-Community com.discordapp.Discord org.qbittorrent.qBittorrent org.onlyoffice.desktopeditors com.github.tchx84.Flatseal
```

- Добавить `exec Hyprland` в конец `/etc/profile` файла для автозапуска композитора после логина в tty (плохо работает. иногда черный экран с указателем. неыохможно взаимодействовать. при нажатии клавиш заверщения работы композитора он выключается, затем снова включается и раюотает без проблем).

- Добавить директорию `getty@tty1.service.d` в `/etc/systemd/system/`.

- Добавить файл `autologin.conf` в `/etc/systemd/system/getty@tty1.service.d/` директрию, сожержащий:
```
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin danimir tty1
```
для автологина в tty1.

- Добавить `--system-title-bar` флаг в `/var/lib/flatpak/app/org.onlyoffice.desktopeditors/current/active/export/share/applications/org.onlyoffice.desktopeditors.desktop` файл в `Exec` секцию.

- Установить oh-my-zsh этой командой:
```sh
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

- Включить bluetooth:
```sh
systemctl enable bluetooth.service; systemctl start bluetooth.service
```

- Включить syncthing:
```sh
syncthing; systemctl enable syncthing@danimir.service; systemctl start syncthing@danimir.service
```

- Добавить ссылки на неовим (необходимо для ranger и git):
```sh
ln -s /bin/nvim /bin/vi; ln -s /bin/nvim /bin/vim
```

- Управление bluetooth соединением можно сделать с помощью wofi.

- Для выпадающих окон for смены раскладки клавиатуры, изменения громкости или яркости можно использовать dunst уведомления.

- Управление интернетом можно сделать с помощью wofi.

- Включить networkmanager:
```sh
systemctl enable NetworkManager
systemctl start NetworkManager
```

- Добавить раскладку клавиатуры в `hyprland.conf`:
```sh
input {
    kb_layout = us,ru
    kb_options = grp:caps_toggle
    }
```

TODO:
перевести с пакмана на nix.
