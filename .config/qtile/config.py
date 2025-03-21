# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration


power = os.path.expanduser('~/.config/qtile/powermenu')
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home)

mod = "mod4"
terminal = guess_terminal()
alt = "mod1"
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "c", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.spawn('dmenu_run -z 1000 -l 15 -nb "#292c35" -p "Run:" -sb "#c179d4" -sf "#292c35"')),
    Key([mod], "e", lazy.spawn('pcmanfm')),
    Key([mod],"Print",lazy.spawn('screengrab')),
    Key([mod],"p", lazy.spawn(power)),
    Key([alt], "Shift_L",  lazy.widget["keyboardlayout"].next_keyboard()),
    Key([mod], "b", lazy.spawn('brave')),
    Key([mod], "s", lazy.spawn('spotify')),
    Key([mod, "shift"], "e", lazy.spawn('emacs')),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


#groups = [Group(i) for i in "123456789"]



#groups = [
    #Group("1"),
    #Group("2"),
    #Group("3", matches=[Match(wm_class=["qutebrowser"])]),
    #]



groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

group_labels = [" ", " ", " ", " ", " ", "6", "7", "8", "9"]
#group_labels = ["DEV", "WWW", "SYS", "DOC", "VBOX", "CHAT", "MUS", "VID", "GFX", "MISC"]
#group_labels = ["", "", "", "", "", "", "𝦝", "", "", "⛨"]
#group_labels = [" ", " ", " ", " ", " ", " ", "⛨ ", " ", " "]




for i in range(len(group_names)):
    groups.append(

        Group(
            name=group_names[i],
            #layout=group_layouts[i].lower(),
            label=group_labels[i],

        ))

@hook.subscribe.client_new
def assign_app_group(client):
    wm_class = client.window.get_wm_class()
    if wm_class in [['brave-browser', 'Brave-browser']]:
        client.togroup("2")
        client.group.cmd_toscreen()
    elif wm_class in [['telegram-desktop', 'TelegramDesktop']]:
        client.togroup("3")
        client.group.cmd_toscreen()
    elif wm_class in [['emacs', 'Emacs']]:
        client.togroup("1")
        client.group.cmd_toscreen()
    elif wm_class in [['steamwebhelper','steam']]:
        client.togroup("4")
        client.group.cmd_toscreen()
    elif wm_class in [['spotify', 'Spotify']]:
        client.togroup("5")

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 2,
                "margin": 0,
                "border_focus": "#5e81ac",
                "border_normal": "4c556a"
                }



layouts = [
    layout.Columns(
        #border_width=2,
        #border_focus = "#5e81ac",
        #border_normal = "#4c556a",
        **layout_theme
    ),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Tile(**layout_theme),
    layout.Max(**layout_theme),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
bg = "#292c35"
color1 = "#45d8fd"
color2 = "#97be66"
color3 = "#c477dc"
color4 = "#da864a"
color5 = "#fc6a6a"
fg = "#45d8fd"
color6 = "#FF79C6"
color7 = "#a9a1e1"
color8 = "#51afef"
color9 = "#F1FA8c"

widget_defaults = dict(
    font="FiraCode Nerd Font Medium",
    fontsize = 13,
    margin_y = 4
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=4),
                widget.Image(
                    filename = "~/.config/qtile/arch.svg",
                    scale = "False",
                    margin_x = 2,
                    margin_y = 2
                 ),

                widget.GroupBox(
                    #font = "Ubuntu Bold",
                    padding_y =4,
                    padding_x = 5,
                    rounded = False,
                    fontsize = 15,
                    borderwidth = 2,
                    active = color2,
                    inactive = color1,
                    this_screen_border = color4,
                    other_current_screen_border = color7,
                    other_screen_border = color4,

                    highlight_color = bg,
                    highlight_method = "line",
                    this_current_screen_border = color3,
                    block_highlight_text_color = color3,
                    background = bg,
                    foreground = fg

                ),
                widget.TextBox(
                    text = '|',
                    foreground = color5,
                    fontsize = 14,
                ),
                widget.CurrentLayout(
                    padding = 5
                 ),

                widget.TextBox(
                    text = '|',
                    foreground = color5,
                    fontsize = 14
                 ),
                widget.WindowName(
                    padding = 4,
                    max_chars = 15
                    ),
                widget.Cmus(

                ),
                widget.Wttr(
                    location={
                        'Your_city':'Home',

                    },
                    format = 3,
                    foreground = color8,

                    decorations = [
                        BorderDecoration (
                            colour = color8,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],
                ),
                widget.GenPollText(
                    update_interval = 300,
                    func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
                    foreground = color6,
                    padding = 6,
                    fmt = ' {}',
                    decorations = [
                        BorderDecoration (
                            colour = color6,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],
                 ),
                widget.CheckUpdates(
                    foreground = color2,
                    colour_have_updates = color7,
                    colour_no_updates = color7,
                    distro = 'Arch_checkupdates',
                    update_interval = 60,
                    display_format = '󰮯 {updates} PKG',
                    fontsize = 15,
                    no_update_string=' NO PKG',
                    decorations = [
                        BorderDecoration (
                            colour = color7,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,
                        )

                    ],

                ),
                widget.CPU(
                    format = ' Cpu:{load_percent}%',
                    foreground = color2,
                    padding = 6,
                    decorations = [
                        BorderDecoration (
                            colour = color2,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],
                 ),
                widget.Memory(
                    foreground = color4,
                    padding = 6,
                    format = '{MemUsed: .0f}{mm}',
                    fmt = ' Mem:{}',
                    decorations = [
                        BorderDecoration (
                            colour = color4,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],
                 ),
                widget.DF(
                    update_interval = 60,
                    foreground = color5,
                    padding = 6,
                    partition = '/home',
                    format = '{uf}{m}',
                    fmt = ' Disk:{}',
                    visible_on_warn = False,
                    decorations = [
                        BorderDecoration (
                            colour = color5,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],
                 ),
                widget.Volume(
                     foreground = color3,
                     padding = 6,
                     fmt = '  {}',
                     step = 1,
                     decorations = [
                        BorderDecoration (
                            colour = color3,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],
                 ),
                widget.Net(
                    interface = "enp5s0",
                    format='󰈁 {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                    foreground = color7,
                    decorations = [
                        BorderDecoration (
                            colour = color7,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],
                ),
                widget.KeyboardLayout(
                    foreground = color2,
                    background = bg,
                    padding = 6,
                    fmt = ' {}',
                    configured_keyboards=['us','ru'],
                    decorations = [
                        BorderDecoration (
                            colour = color2,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],

                 ),

                widget.Clock(
                    foreground = color1,
                    padding = 6,
                    format = " %a %b %d-%I:%M %p",
                    decorations = [
                        BorderDecoration (
                            colour = color1,
                            border_width = [0,0,3,0],
                            padding_x = 5,
                            padding_y = None,

                        )
                    ],
                 ),




                widget.Systray(),
                widget.Spacer(length = 2),
            ],
            29,
            background = bg,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus = "#5e81ac",
    border_normal = "4c556a"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
