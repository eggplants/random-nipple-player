import tkinter as tk
from subprocess import Popen as Popen
from tkinter import filedialog as filedialog, ttk
from tkinter.colorchooser import askcolor as askcolor
from typing import Any, List

version: str
ver: Any
port: str
tclversion_detailed: Any
framework_version = tclversion_detailed
webbrowser_available: bool
g_time_start: int
g_time_end: int
g_time_delta: int

def timer_start() -> None: ...
def timer_stop(): ...

MAX_TIMEIT_COUNT: int

def running_linux(): ...
def running_mac(): ...
def running_windows(): ...
def running_trinket(): ...

DEFAULT_BASE64_ICON: bytes
DEFAULT_BASE64_ICON_16_BY_16: bytes
DEFAULT_BASE64_LOADING_GIF: bytes
PSG_DEBUGGER_LOGO: bytes
DEFAULT_WINDOW_ICON = DEFAULT_BASE64_ICON
DEFAULT_ELEMENT_SIZE: Any
DEFAULT_BUTTON_ELEMENT_SIZE: Any
DEFAULT_MARGINS: Any
DEFAULT_ELEMENT_PADDING: Any
DEFAULT_AUTOSIZE_TEXT: bool
DEFAULT_AUTOSIZE_BUTTONS: bool
DEFAULT_FONT: Any
DEFAULT_TEXT_JUSTIFICATION: str
DEFAULT_BORDER_WIDTH: int
DEFAULT_AUTOCLOSE_TIME: int
DEFAULT_DEBUG_WINDOW_SIZE: Any
DEFAULT_WINDOW_LOCATION: Any
MAX_SCROLLED_TEXT_BOX_HEIGHT: int
DEFAULT_TOOLTIP_TIME: int
DEFAULT_TOOLTIP_OFFSET: Any
TOOLTIP_BACKGROUND_COLOR: str
TOOLTIP_FONT: Any
BLUES: Any
PURPLES: Any
GREENS: Any
YELLOWS: Any
TANS: Any
NICE_BUTTON_COLORS: Any
COLOR_SYSTEM_DEFAULT: str
DEFAULT_BUTTON_COLOR: Any
OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR: Any
OFFICIAL_PYSIMPLEGUI_THEME: str
CURRENT_LOOK_AND_FEEL: str
DEFAULT_ERROR_BUTTON_COLOR: Any
DEFAULT_BACKGROUND_COLOR: Any
DEFAULT_ELEMENT_BACKGROUND_COLOR: Any
DEFAULT_ELEMENT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR: Any
DEFAULT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_INPUT_ELEMENTS_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_INPUT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_SCROLLBAR_COLOR: Any
RELIEF_RAISED: str
RELIEF_SUNKEN: str
RELIEF_FLAT: str
RELIEF_RIDGE: str
RELIEF_GROOVE: str
RELIEF_SOLID: str
THEME_DEFAULT: str
THEME_WINNATIVE: str
THEME_CLAM: str
THEME_ALT: str
THEME_CLASSIC: str
THEME_VISTA: str
THEME_XPNATIVE: str
THEME_LIST: Any
DEFAULT_TTK_THEME = THEME_DEFAULT
USE_TTK_BUTTONS: Any
DEFAULT_PROGRESS_BAR_COLOR: Any
DEFAULT_PROGRESS_BAR_COMPUTE: Any
DEFAULT_PROGRESS_BAR_COLOR_OFFICIAL: Any
DEFAULT_PROGRESS_BAR_SIZE: Any
DEFAULT_PROGRESS_BAR_BORDER_WIDTH: int
DEFAULT_PROGRESS_BAR_RELIEF = RELIEF_GROOVE
PROGRESS_BAR_STYLES: Any
DEFAULT_PROGRESS_BAR_STYLE = DEFAULT_TTK_THEME
DEFAULT_METER_ORIENTATION: str
DEFAULT_SLIDER_ORIENTATION: str
DEFAULT_SLIDER_BORDER_WIDTH: int
DEFAULT_SLIDER_RELIEF: Any
DEFAULT_FRAME_RELIEF: Any
DEFAULT_LISTBOX_SELECT_MODE: Any
SELECT_MODE_MULTIPLE: Any
LISTBOX_SELECT_MODE_MULTIPLE: str
SELECT_MODE_BROWSE: Any
LISTBOX_SELECT_MODE_BROWSE: str
SELECT_MODE_EXTENDED: Any
LISTBOX_SELECT_MODE_EXTENDED: str
SELECT_MODE_SINGLE: Any
LISTBOX_SELECT_MODE_SINGLE: str
TABLE_SELECT_MODE_NONE: Any
TABLE_SELECT_MODE_BROWSE: Any
TABLE_SELECT_MODE_EXTENDED: Any
DEFAULT_TABLE_SELECT_MODE = TABLE_SELECT_MODE_EXTENDED
TITLE_LOCATION_TOP: Any
TITLE_LOCATION_BOTTOM: Any
TITLE_LOCATION_LEFT: Any
TITLE_LOCATION_RIGHT: Any
TITLE_LOCATION_TOP_LEFT: Any
TITLE_LOCATION_TOP_RIGHT: Any
TITLE_LOCATION_BOTTOM_LEFT: Any
TITLE_LOCATION_BOTTOM_RIGHT: Any
TEXT_LOCATION_TOP: Any
TEXT_LOCATION_BOTTOM: Any
TEXT_LOCATION_LEFT: Any
TEXT_LOCATION_RIGHT: Any
TEXT_LOCATION_TOP_LEFT: Any
TEXT_LOCATION_TOP_RIGHT: Any
TEXT_LOCATION_BOTTOM_LEFT: Any
TEXT_LOCATION_BOTTOM_RIGHT: Any
TEXT_LOCATION_CENTER: Any
GRAB_ANYWHERE_IGNORE_THESE_WIDGETS: Any
ThisRow: int
MESSAGE_BOX_LINE_WIDTH: int
EVENT_TIMEOUT: str
TIMEOUT_EVENT: str
TIMEOUT_KEY: str
WIN_CLOSED: Any
WINDOW_CLOSED: Any
WINDOW_CLOSE_ATTEMPTED_EVENT: str
WIN_X_EVENT: str
WIN_CLOSE_ATTEMPTED_EVENT: str
TITLEBAR_MINIMIZE_KEY: str
TITLEBAR_MAXIMIZE_KEY: str
TITLEBAR_CLOSE_KEY: str
TITLEBAR_IMAGE_KEY: str
TITLEBAR_DO_NOT_USE_AN_ICON: str
WRITE_ONLY_KEY: str
MENU_DISABLED_CHARACTER: str
MENU_SHORTCUT_CHARACTER: str
MENU_KEY_SEPARATOR: str
MENU_SEPARATOR_LINE: str
MENU_RIGHT_CLICK_EDITME_EXIT: Any
MENU_RIGHT_CLICK_EDITME_VER_EXIT: Any
MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT: Any
MENU_RIGHT_CLICK_EXIT: Any
MENU_RIGHT_CLICK_DISABLED: Any
ENABLE_TK_WINDOWS: bool
USE_CUSTOM_TITLEBAR: bool
CUSTOM_TITLEBAR_BACKGROUND_COLOR: Any
CUSTOM_TITLEBAR_TEXT_COLOR: Any
CUSTOM_TITLEBAR_ICON: Any
CUSTOM_TITLEBAR_FONT: Any
TITLEBAR_METADATA_MARKER: str
CUSTOM_MENUBAR_METADATA_MARKER: str
SUPPRESS_ERROR_POPUPS: bool
SUPPRESS_RAISE_KEY_ERRORS: bool
SUPPRESS_KEY_GUESSING: bool
ENABLE_TREEVIEW_869_PATCH: bool
ENABLE_MAC_NOTITLEBAR_PATCH: bool
OLD_TABLE_TREE_SELECTED_ROW_COLORS: Any
ALTERNATE_TABLE_AND_TREE_SELECTED_ROW_COLORS: Any
SYMBOL_SQUARE: str
SYMBOL_CIRCLE: str
SYMBOL_CIRCLE_OUTLINE: str
SYMBOL_UP: str
SYMBOL_RIGHT: str
SYMBOL_LEFT: str
SYMBOL_DOWN: str
SYMBOL_X: str
SYMBOL_CHECK: str
SYMBOL_BALLOT_X: str
SYMBOL_BALLOT_CHECK: str
SYMBOL_LEFT_DOUBLE: str
SYMBOL_RIGHT_DOUBLE: str
SYMBOL_LEFT_ARROWHEAD: str
SYMBOL_RIGHT_ARROWHEAD: str
SYMBOL_UP_ARROWHEAD: str
SYMBOL_DOWN_ARROWHEAD: str
SYMBOL_TITLEBAR_MINIMIZE: str
SYMBOL_TITLEBAR_MAXIMIZE: str
SYMBOL_TITLEBAR_CLOSE: str
DEFAULT_USER_SETTINGS_WIN_PATH: str
DEFAULT_USER_SETTINGS_LINUX_PATH: str
DEFAULT_USER_SETTINGS_MAC_PATH: str
DEFAULT_USER_SETTINGS_UNKNOWN_OS_PATH: str
DEFAULT_USER_SETTINGS_PATH: Any
DEFAULT_USER_SETTINGS_PYSIMPLEGUI_PATH: Any
DEFAULT_USER_SETTINGS_PYSIMPLEGUI_FILENAME: str

def rgb(red, green, blue): ...

BUTTON_TYPE_BROWSE_FOLDER: int
BUTTON_TYPE_BROWSE_FILE: int
BUTTON_TYPE_BROWSE_FILES: int
BUTTON_TYPE_SAVEAS_FILE: int
BUTTON_TYPE_CLOSES_WIN: int
BUTTON_TYPE_CLOSES_WIN_ONLY: int
BUTTON_TYPE_READ_FORM: int
BUTTON_TYPE_REALTIME: int
BUTTON_TYPE_CALENDAR_CHOOSER: int
BUTTON_TYPE_COLOR_CHOOSER: int
BUTTON_TYPE_SHOW_DEBUGGER: int
BROWSE_FILES_DELIMITER: str
BUTTON_DISABLED_MEANS_IGNORE: str
ELEM_TYPE_TEXT: str
ELEM_TYPE_INPUT_TEXT: str
ELEM_TYPE_INPUT_COMBO: str
ELEM_TYPE_INPUT_OPTION_MENU: str
ELEM_TYPE_INPUT_RADIO: str
ELEM_TYPE_INPUT_MULTILINE: str
ELEM_TYPE_INPUT_CHECKBOX: str
ELEM_TYPE_INPUT_SPIN: str
ELEM_TYPE_BUTTON: str
ELEM_TYPE_IMAGE: str
ELEM_TYPE_CANVAS: str
ELEM_TYPE_FRAME: str
ELEM_TYPE_GRAPH: str
ELEM_TYPE_TAB: str
ELEM_TYPE_TAB_GROUP: str
ELEM_TYPE_INPUT_SLIDER: str
ELEM_TYPE_INPUT_LISTBOX: str
ELEM_TYPE_OUTPUT: str
ELEM_TYPE_COLUMN: str
ELEM_TYPE_MENUBAR: str
ELEM_TYPE_PROGRESS_BAR: str
ELEM_TYPE_BLANK: str
ELEM_TYPE_TABLE: str
ELEM_TYPE_TREE: str
ELEM_TYPE_ERROR: str
ELEM_TYPE_SEPARATOR: str
ELEM_TYPE_STATUSBAR: str
ELEM_TYPE_PANE: str
ELEM_TYPE_BUTTONMENU: str
ELEM_TYPE_TITLEBAR: str
ELEM_TYPE_SIZEGRIP: str
POPUP_BUTTONS_YES_NO: int
POPUP_BUTTONS_CANCELLED: int
POPUP_BUTTONS_ERROR: int
POPUP_BUTTONS_OK_CANCEL: int
POPUP_BUTTONS_OK: int
POPUP_BUTTONS_NO_BUTTONS: int

class ToolTip:
    widget: Any
    text: Any
    timeout: Any
    tipwindow: Any
    id: Any
    x: int
    def __init__(self, widget, text, timeout=...) -> None: ...
    y: Any
    def enter(self, event: Any | None = ...) -> None: ...
    def leave(self, event: Any | None = ...) -> None: ...
    def schedule(self) -> None: ...
    def unschedule(self) -> None: ...
    def showtip(self) -> None: ...
    def hidetip(self) -> None: ...

class Element:
    Size: Any
    Type: Any
    AutoSizeText: Any
    Pad: Any
    Font: Any
    TKStringVar: Any
    TKIntVar: Any
    TKText: Any
    TKEntry: Any
    TKImage: Any
    ParentForm: Any
    ParentContainer: Any
    TextInputDefault: Any
    Position: Any
    BackgroundColor: Any
    TextColor: Any
    Key: Any
    Tooltip: Any
    TooltipObject: Any
    TKRightClickMenu: Any
    Widget: Any
    Tearoff: bool
    ParentRowFrame: Any
    user_bind_dict: Any
    user_bind_event: Any
    pad_used: Any
    DisabledTextColor: Any
    ItemFont: Any
    def __init__(self, type, size=..., auto_size_text: Any | None = ..., font: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., key: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    @property
    def visible(self): ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, value) -> None: ...
    def bind(self, bind_string, key_modifier): ...
    def unbind(self, bind_string) -> None: ...
    def set_tooltip(self, tooltip_text) -> None: ...
    def set_focus(self, force: bool = ...) -> None: ...
    def block_focus(self, block: bool = ...) -> None: ...
    def set_size(self, size=...) -> None: ...
    def get_size(self): ...
    def hide_row(self) -> None: ...
    def unhide_row(self) -> None: ...
    def expand(self, expand_x: bool = ..., expand_y: bool = ..., expand_row: bool = ...) -> None: ...
    def set_cursor(self, cursor: Any | None = ..., cursor_color: Any | None = ...) -> None: ...
    def set_vscroll_position(self, percent_from_top) -> None: ...
    def grab_anywhere_exclude(self) -> None: ...
    def grab_anywhere_include(self) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def __call__(self, *args, **kwargs): ...
    SetTooltip: Any
    SetFocus: Any

class Input(Element):
    DefaultText: Any
    PasswordCharacter: Any
    Focus: Any
    do_not_clear: Any
    Justification: Any
    Disabled: Any
    ChangeSubmits: Any
    RightClickMenu: Any
    UseReadonlyForDisable: Any
    disabled_readonly_background_color: Any
    disabled_readonly_text_color: Any
    ReadOnly: Any
    BorderWidth: Any
    TKEntry: Any
    def __init__(self, default_text: str = ..., size=..., s=..., disabled: bool = ..., password_char: str = ..., justification: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., font: Any | None = ..., tooltip: Any | None = ..., border_width: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., do_not_clear: bool = ..., key: Any | None = ..., k: Any | None = ..., focus: bool = ..., pad: Any | None = ..., use_readonly_for_disable: bool = ..., readonly: bool = ..., disabled_readonly_background_color: Any | None = ..., disabled_readonly_text_color: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, value: Any | None = ..., disabled: Any | None = ..., select: Any | None = ..., visible: Any | None = ..., text_color: Any | None = ..., background_color: Any | None = ..., move_cursor_to: str = ..., password_char: Any | None = ...) -> None: ...
    def get(self): ...
    Get: Any
    Update: Any
In = Input
InputText = Input
I = Input

class Combo(Element):
    Values: Any
    DefaultValue: Any
    ChangeSubmits: Any
    Widget: Any
    Disabled: Any
    Readonly: Any
    BindReturnKey: Any
    def __init__(self, values, default_value: Any | None = ..., size=..., s=..., auto_size_text: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., bind_return_key: bool = ..., change_submits: bool = ..., enable_events: bool = ..., disabled: bool = ..., key: Any | None = ..., k: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., readonly: bool = ..., font: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, value: Any | None = ..., values: Any | None = ..., set_to_index: Any | None = ..., disabled: Any | None = ..., readonly: Any | None = ..., font: Any | None = ..., visible: Any | None = ..., size=...) -> None: ...
    def get(self): ...
    Get: Any
    Update: Any
InputCombo = Combo
DropDown = InputCombo
Drop = InputCombo
DD = Combo

class OptionMenu(Element):
    Values: Any
    DefaultValue: Any
    Widget: Any
    Disabled: Any
    def __init__(self, values, default_value: Any | None = ..., size=..., s=..., disabled: bool = ..., auto_size_text: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., key: Any | None = ..., k: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, value: Any | None = ..., values: Any | None = ..., disabled: Any | None = ..., visible: Any | None = ..., size=...) -> None: ...
    Update: Any
InputOptionMenu = OptionMenu

class Listbox(Element):
    Values: Any
    DefaultValues: Any
    TKListbox: Any
    ChangeSubmits: Any
    BindReturnKey: Any
    Disabled: Any
    SelectMode: Any
    HighlightBackgroundColor: Any
    HighlightTextColor: Any
    RightClickMenu: Any
    vsb: Any
    element_frame: Any
    NoScrollbar: Any
    def __init__(self, values, default_values: Any | None = ..., select_mode: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., bind_return_key: bool = ..., size=..., s=..., disabled: bool = ..., auto_size_text: Any | None = ..., font: Any | None = ..., no_scrollbar: bool = ..., background_color: Any | None = ..., text_color: Any | None = ..., highlight_background_color: Any | None = ..., highlight_text_color: Any | None = ..., key: Any | None = ..., k: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, values: Any | None = ..., disabled: Any | None = ..., set_to_index: Any | None = ..., scroll_to_index: Any | None = ..., select_mode: Any | None = ..., visible: Any | None = ...) -> None: ...
    def set_value(self, values) -> None: ...
    def get_list_values(self) -> List[Any]: ...
    def get_indexes(self): ...
    def get(self): ...
    GetIndexes: Any
    GetListValues: Any
    SetValue: Any
    Update: Any
LBox = Listbox
LB = Listbox

class Radio(Element):
    InitialState: Any
    Text: Any
    Widget: Any
    GroupID: Any
    Value: Any
    Disabled: Any
    TextColor: Any
    CircleBackgroundColor: Any
    ChangeSubmits: Any
    EncodedRadioValue: Any
    def __init__(self, text, group_id, default: bool = ..., disabled: bool = ..., size=..., s=..., auto_size_text: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., circle_color: Any | None = ..., font: Any | None = ..., key: Any | None = ..., k: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    BackgroundColor: Any
    def update(self, value: Any | None = ..., text: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., circle_color: Any | None = ..., disabled: Any | None = ..., visible: Any | None = ...) -> None: ...
    def reset_group(self) -> None: ...
    def get(self) -> bool: ...
    Get: Any
    ResetGroup: Any
    Update: Any
R = Radio
Rad = Radio

class Checkbox(Element):
    Text: Any
    InitialState: Any
    Value: Any
    TKCheckbutton: Any
    Disabled: Any
    TextColor: Any
    CheckboxBackgroundColor: Any
    ChangeSubmits: Any
    def __init__(self, text, default: bool = ..., size=..., s=..., auto_size_text: Any | None = ..., font: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., checkbox_color: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., disabled: bool = ..., key: Any | None = ..., k: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def get(self) -> bool: ...
    BackgroundColor: Any
    def update(self, value: Any | None = ..., text: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., checkbox_color: Any | None = ..., disabled: Any | None = ..., visible: Any | None = ...) -> None: ...
    Get: Any
    Update: Any
CB = Checkbox
CBox = Checkbox
Check = Checkbox

class Spin(Element):
    Values: Any
    DefaultValue: Any
    ChangeSubmits: Any
    TKSpinBox: Any
    Disabled: Any
    Readonly: Any
    def __init__(self, values, initial_value: Any | None = ..., disabled: bool = ..., change_submits: bool = ..., enable_events: bool = ..., readonly: bool = ..., size=..., s=..., auto_size_text: Any | None = ..., font: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., key: Any | None = ..., k: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, value: Any | None = ..., values: Any | None = ..., disabled: Any | None = ..., readonly: Any | None = ..., visible: Any | None = ...) -> None: ...
    def get(self): ...
    Get: Any
    Update: Any

Sp: Spin

class Multiline(Element):
    DefaultText: Any
    EnterSubmits: Any
    Focus: Any
    do_not_clear: Any
    Autoscroll: Any
    Disabled: Any
    ChangeSubmits: Any
    RightClickMenu: Any
    BorderWidth: Any
    TagCounter: int
    TKText: Any
    tags: Any
    WriteOnly: Any
    AutoRefresh: Any
    previous_stdout: Any
    previous_stderr: Any
    reroute_cprint: Any
    echo_stdout_stderr: Any
    Justification: Any
    justification_tag: Any
    expand_x: Any
    expand_y: Any
    no_scrollbar: Any
    def __init__(self, default_text: str = ..., enter_submits: bool = ..., disabled: bool = ..., autoscroll: bool = ..., border_width: Any | None = ..., size=..., s=..., auto_size_text: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., do_not_clear: bool = ..., key: Any | None = ..., k: Any | None = ..., write_only: bool = ..., auto_refresh: bool = ..., reroute_stdout: bool = ..., reroute_stderr: bool = ..., reroute_cprint: bool = ..., echo_stdout_stderr: bool = ..., focus: bool = ..., font: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., justification: Any | None = ..., no_scrollbar: bool = ..., expand_x: bool = ..., expand_y: bool = ..., right_click_menu: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, value: Any | None = ..., disabled: Any | None = ..., append: bool = ..., font: Any | None = ..., text_color: Any | None = ..., background_color: Any | None = ..., text_color_for_value: Any | None = ..., background_color_for_value: Any | None = ..., visible: Any | None = ..., autoscroll: Any | None = ..., justification: Any | None = ..., font_for_value: Any | None = ...) -> None: ...
    def get(self): ...
    def print(self, *args, end: Any | None = ..., sep: Any | None = ..., text_color: Any | None = ..., background_color: Any | None = ..., justification: Any | None = ..., font: Any | None = ..., colors: Any | None = ..., t: Any | None = ..., b: Any | None = ..., c: Any | None = ...) -> None: ...
    def reroute_stdout_to_here(self) -> None: ...
    def reroute_stderr_to_here(self) -> None: ...
    def restore_stdout(self) -> None: ...
    def restore_stderr(self) -> None: ...
    def write(self, txt) -> None: ...
    def flush(self) -> None: ...
    def __del__(self) -> None: ...
    Get: Any
    Update: Any
ML = Multiline
MLine = Multiline

class Text(Element):
    DisplayText: Any
    TextColor: Any
    Justification: Any
    Relief: Any
    ClickSubmits: Any
    RightClickMenu: Any
    TKRightClickMenu: Any
    BorderWidth: Any
    Grab: Any
    def __init__(self, text: str = ..., size=..., s=..., auto_size_text: Any | None = ..., click_submits: bool = ..., enable_events: bool = ..., relief: Any | None = ..., font: Any | None = ..., text_color: Any | None = ..., background_color: Any | None = ..., border_width: Any | None = ..., justification: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., right_click_menu: Any | None = ..., grab: Any | None = ..., tooltip: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, value: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., font: Any | None = ..., visible: Any | None = ...) -> None: ...
    def get(self): ...
    @classmethod
    def char_width_in_pixels(cls, font, character: str = ...): ...
    @classmethod
    def char_height_in_pixels(cls, font): ...
    @classmethod
    def string_width_in_pixels(cls, font, string): ...
    Get: Any
    Update: Any

Txt: Text
T: Text

class StatusBar(Element):
    DisplayText: Any
    TextColor: Any
    Justification: Any
    Relief: Any
    ClickSubmits: Any
    TKText: Any
    RightClickMenu: Any
    def __init__(self, text, size=..., s=..., auto_size_text: Any | None = ..., click_submits: Any | None = ..., enable_events: bool = ..., relief=..., font: Any | None = ..., text_color: Any | None = ..., background_color: Any | None = ..., justification: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., right_click_menu: Any | None = ..., tooltip: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, value: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., font: Any | None = ..., visible: Any | None = ...) -> None: ...
    Update: Any
SBar = StatusBar

class TKProgressBar:
    uniqueness_counter: int
    Length: Any
    Width: Any
    Max: Any
    Orientation: Any
    Count: Any
    PriorCount: int
    StyleName: str
    style_name: Any
    TKProgressBarForReal: Any
    def __init__(self, root, max, length: int = ..., width=..., style=..., relief=..., border_width=..., orientation: str = ..., BarColor=..., key: Any | None = ...) -> None: ...
    def Update(self, count: Any | None = ..., max: Any | None = ...): ...

class TKOutput(tk.Frame):
    frame: Any
    output: Any
    vsb: Any
    previous_stdout: Any
    previous_stderr: Any
    parent: Any
    echo_stdout_stderr: Any
    def __init__(self, parent, width, height, bd, background_color: Any | None = ..., text_color: Any | None = ..., echo_stdout_stderr: bool = ..., font: Any | None = ..., pad: Any | None = ...) -> None: ...
    def write(self, txt) -> None: ...
    def Close(self) -> None: ...
    def flush(self) -> None: ...
    def __del__(self) -> None: ...

class Output(Element):
    RightClickMenu: Any
    echo_stdout_stderr: Any
    def __init__(self, size=..., s=..., background_color: Any | None = ..., text_color: Any | None = ..., pad: Any | None = ..., echo_stdout_stderr: bool = ..., font: Any | None = ..., tooltip: Any | None = ..., key: Any | None = ..., k: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    @property
    def tk_out(self): ...
    def update(self, value: Any | None = ..., visible: Any | None = ...) -> None: ...
    def get(self): ...
    def expand(self, expand_x: bool = ..., expand_y: bool = ..., expand_row: bool = ...) -> None: ...
    def __del__(self) -> None: ...
    TKOut: Any
    Update: Any
    Get: Any

class Button(Element):
    AutoSizeButton: Any
    BType: Any
    FileTypes: Any
    Widget: Any
    Target: Any
    ButtonText: Any
    RightClickMenu: Any
    ButtonColor: Any
    DisabledButtonColor: Any
    ImageFilename: Any
    ImageData: Any
    ImageSize: Any
    ImageSubsample: Any
    UserData: Any
    BorderWidth: Any
    BindReturnKey: Any
    Focus: Any
    TKCal: Any
    calendar_default_date_M_D_Y: Any
    calendar_close_when_chosen: bool
    calendar_locale: Any
    calendar_format: Any
    calendar_location: Any
    calendar_no_titlebar: bool
    calendar_begin_at_sunday_plus: int
    calendar_month_names: Any
    calendar_day_abbreviations: Any
    calendar_title: str
    calendar_selection: str
    InitialFolder: Any
    DefaultExtension: Any
    Disabled: Any
    ChangeSubmits: Any
    UseTtkButtons: Any
    HighlightColors: Any
    MouseOverColors: Any
    def __init__(self, button_text: str = ..., button_type=..., target=..., tooltip: Any | None = ..., file_types=..., initial_folder: Any | None = ..., default_extension: str = ..., disabled: bool = ..., change_submits: bool = ..., enable_events: bool = ..., image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., border_width: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled_button_color: Any | None = ..., highlight_colors: Any | None = ..., mouseover_colors=..., use_ttk_buttons: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    LastButtonClickedWasRealtime: bool
    def ButtonReleaseCallBack(self, parm) -> None: ...
    def ButtonPressCallBack(self, parm) -> None: ...
    def ButtonCallBack(self) -> None: ...
    def update(self, text: Any | None = ..., button_color=..., disabled: Any | None = ..., image_data: Any | None = ..., image_filename: Any | None = ..., visible: Any | None = ..., image_subsample: Any | None = ..., disabled_button_color=..., image_size: Any | None = ...) -> None: ...
    def get_text(self): ...
    def click(self) -> None: ...
    Click: Any
    GetText: Any
    Update: Any
B = Button
Btn = Button

class ButtonMenu(Element):
    MenuDefinition: Any
    AutoSizeButton: Any
    ButtonText: Any
    ButtonColor: Any
    BackgroundColor: Any
    TextColor: Any
    DisabledTextColor: Any
    ItemFont: Any
    BorderWidth: Any
    ImageFilename: Any
    ImageData: Any
    ImageSize: Any
    ImageSubsample: Any
    Disabled: Any
    IsButtonMenu: bool
    MenuItemChosen: Any
    TKButtonMenu: Any
    TKMenu: Any
    part_of_custom_menubar: bool
    custom_menubar_key: Any
    Tearoff: Any
    def __init__(self, button_text, menu_def, tooltip: Any | None = ..., disabled: bool = ..., image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., border_width: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., text_color: Any | None = ..., background_color: Any | None = ..., disabled_text_color: Any | None = ..., font: Any | None = ..., item_font: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., tearoff: bool = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, menu_definition, visible: Any | None = ...) -> None: ...
    def Click(self) -> None: ...
    Update: Any
BMenu = ButtonMenu
BM = ButtonMenu

class ProgressBar(Element):
    MaxValue: Any
    TKProgressBar: Any
    Cancelled: bool
    NotRunning: bool
    Orientation: Any
    BarColor: Any
    BarStyle: Any
    BorderWidth: Any
    Relief: Any
    BarExpired: bool
    def __init__(self, max_value, orientation: Any | None = ..., size=..., s=..., auto_size_text: Any | None = ..., bar_color: Any | None = ..., style: Any | None = ..., border_width: Any | None = ..., relief: Any | None = ..., key: Any | None = ..., k: Any | None = ..., pad: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update_bar(self, current_count, max: Any | None = ...): ...
    def update(self, current_count, max: Any | None = ..., visible: Any | None = ...): ...
    Update: Any
    UpdateBar: Any
PBar = ProgressBar
Prog = ProgressBar
Progress = ProgressBar

class Image(Element):
    Filename: Any
    Data: Any
    Widget: Any
    BackgroundColor: Any
    EnableEvents: Any
    RightClickMenu: Any
    AnimatedFrames: Any
    CurrentFrameNumber: int
    TotalAnimatedFrames: int
    LastFrameTime: int
    Source: Any
    def __init__(self, filename: Any | None = ..., data: Any | None = ..., background_color: Any | None = ..., size=..., s=..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., tooltip: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., enable_events: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, filename: Any | None = ..., data: Any | None = ..., size=..., visible: Any | None = ...) -> None: ...
    def update_animation(self, source, time_between_frames: int = ...) -> None: ...
    frame_num: int
    image: Any
    def update_animation_no_buffering(self, source, time_between_frames: int = ...) -> None: ...
    Update: Any
    UpdateAnimation: Any
Im = Image

class Canvas(Element):
    BackgroundColor: Any
    RightClickMenu: Any
    BorderWidth: Any
    def __init__(self, canvas: Any | None = ..., background_color: Any | None = ..., size=..., s=..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., tooltip: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., border_width: int = ..., metadata: Any | None = ...) -> None: ...
    @property
    def tk_canvas(self): ...
    TKCanvas: Any

class Graph(Element):
    CanvasSize: Any
    BottomLeft: Any
    TopRight: Any
    ChangeSubmits: Any
    DragSubmits: Any
    ClickPosition: Any
    MouseButtonDown: bool
    Images: Any
    RightClickMenu: Any
    FloatValues: Any
    BorderWidth: Any
    def __init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color: Any | None = ..., pad: Any | None = ..., change_submits: bool = ..., drag_submits: bool = ..., enable_events: bool = ..., key: Any | None = ..., k: Any | None = ..., tooltip: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., float_values: bool = ..., border_width: int = ..., metadata: Any | None = ...) -> None: ...
    def draw_line(self, point_from, point_to, color: str = ..., width: int = ...): ...
    def draw_lines(self, points, color: str = ..., width: int = ...): ...
    def draw_point(self, point, size: int = ..., color: str = ...): ...
    def draw_circle(self, center_location, radius, fill_color: Any | None = ..., line_color: str = ..., line_width: int = ...): ...
    def draw_oval(self, top_left, bottom_right, fill_color: Any | None = ..., line_color: Any | None = ..., line_width: int = ...): ...
    def draw_arc(self, top_left, bottom_right, extent, start_angle, style: Any | None = ..., arc_color: str = ..., line_width: int = ..., fill_color: Any | None = ...): ...
    def draw_rectangle(self, top_left, bottom_right, fill_color: Any | None = ..., line_color: Any | None = ..., line_width: Any | None = ...): ...
    def draw_polygon(self, points, fill_color: Any | None = ..., line_color: Any | None = ..., line_width: Any | None = ...): ...
    def draw_text(self, text, location, color: str = ..., font: Any | None = ..., angle: int = ..., text_location=...): ...
    def draw_image(self, filename: Any | None = ..., data: Any | None = ..., location=...): ...
    def erase(self) -> None: ...
    def delete_figure(self, id) -> None: ...
    def update(self, background_color: Any | None = ..., visible: Any | None = ...) -> None: ...
    def move(self, x_direction, y_direction) -> None: ...
    def move_figure(self, figure, x_direction, y_direction) -> None: ...
    def relocate_figure(self, figure, x, y) -> None: ...
    def send_figure_to_back(self, figure) -> None: ...
    def bring_figure_to_front(self, figure) -> None: ...
    def get_figures_at_location(self, location): ...
    def get_bounding_box(self, figure): ...
    def change_coordinates(self, graph_bottom_left, graph_top_right) -> None: ...
    @property
    def tk_canvas(self): ...
    LastButtonClickedWasRealtime: Any
    def button_release_call_back(self, event) -> None: ...
    def button_press_call_back(self, event) -> None: ...
    def motion_call_back(self, event) -> None: ...
    BringFigureToFront: Any
    ButtonPressCallBack: Any
    ButtonReleaseCallBack: Any
    DeleteFigure: Any
    DrawArc: Any
    DrawCircle: Any
    DrawImage: Any
    DrawLine: Any
    DrawOval: Any
    DrawPoint: Any
    DrawPolygon: Any
    DrawLines: Any
    DrawRectangle: Any
    DrawText: Any
    GetFiguresAtLocation: Any
    GetBoundingBox: Any
    Erase: Any
    MotionCallBack: Any
    Move: Any
    MoveFigure: Any
    RelocateFigure: Any
    SendFigureToBack: Any
    TKCanvas: Any
    Update: Any
G = Graph

class Frame(Element):
    UseDictionary: bool
    ReturnValues: Any
    ReturnValuesList: Any
    ReturnValuesDictionary: Any
    DictionaryKeyCounter: int
    ParentWindow: Any
    Rows: Any
    TKFrame: Any
    Title: Any
    Relief: Any
    TitleLocation: Any
    BorderWidth: Any
    BackgroundColor: Any
    RightClickMenu: Any
    ContainerElemementNumber: Any
    ElementJustification: Any
    VerticalAlignment: Any
    Widget: Any
    def __init__(self, title, layout, title_color: Any | None = ..., background_color: Any | None = ..., title_location: Any | None = ..., relief=..., size=..., s=..., font: Any | None = ..., pad: Any | None = ..., border_width: Any | None = ..., key: Any | None = ..., k: Any | None = ..., tooltip: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., element_justification: str = ..., vertical_alignment: Any | None = ..., metadata: Any | None = ...) -> None: ...
    def add_row(self, *args) -> None: ...
    def layout(self, rows): ...
    def update(self, value: Any | None = ..., visible: Any | None = ...) -> None: ...
    AddRow: Any
    Layout: Any
    Update: Any
Fr = Frame

class VerticalSeparator(Element):
    Orientation: str
    color: Any
    def __init__(self, color: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ...) -> None: ...
VSeperator = VerticalSeparator
VSeparator = VerticalSeparator
VSep = VerticalSeparator

class HorizontalSeparator(Element):
    Orientation: str
    color: Any
    def __init__(self, color: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ...) -> None: ...
HSeparator = HorizontalSeparator
HSep = HorizontalSeparator

class Sizegrip(Element):
    def __init__(self, background_color: Any | None = ...) -> None: ...
SGrip = Sizegrip

class Tab(Element):
    UseDictionary: bool
    ReturnValues: Any
    ReturnValuesList: Any
    ReturnValuesDictionary: Any
    DictionaryKeyCounter: int
    ParentWindow: Any
    Rows: Any
    TKFrame: Any
    Widget: Any
    Title: Any
    BorderWidth: Any
    Disabled: Any
    ParentNotebook: Any
    TabID: Any
    BackgroundColor: Any
    RightClickMenu: Any
    ContainerElemementNumber: Any
    ElementJustification: Any
    def __init__(self, title, layout, title_color: Any | None = ..., background_color: Any | None = ..., font: Any | None = ..., pad: Any | None = ..., disabled: bool = ..., border_width: Any | None = ..., key: Any | None = ..., k: Any | None = ..., tooltip: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., element_justification: str = ..., metadata: Any | None = ...) -> None: ...
    def add_row(self, *args) -> None: ...
    def layout(self, rows): ...
    def update(self, title: Any | None = ..., disabled: Any | None = ..., visible: Any | None = ...): ...
    def select(self) -> None: ...
    AddRow: Any
    Layout: Any
    Select: Any
    Update: Any

class TabGroup(Element):
    UseDictionary: bool
    ReturnValues: Any
    ReturnValuesList: Any
    ReturnValuesDictionary: Any
    DictionaryKeyCounter: int
    ParentWindow: Any
    SelectedTitleColor: Any
    SelectedBackgroundColor: Any
    TabBackgroundColor: Any
    Rows: Any
    TKNotebook: Any
    Widget: Any
    TabCount: int
    BorderWidth: Any
    BackgroundColor: Any
    ChangeSubmits: Any
    TabLocation: Any
    ElementJustification: str
    def __init__(self, layout, tab_location: Any | None = ..., title_color: Any | None = ..., tab_background_color: Any | None = ..., selected_title_color: Any | None = ..., selected_background_color: Any | None = ..., background_color: Any | None = ..., font: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., pad: Any | None = ..., border_width: Any | None = ..., theme: Any | None = ..., key: Any | None = ..., k: Any | None = ..., size=..., s=..., tooltip: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def add_row(self, *args) -> None: ...
    def layout(self, rows): ...
    def find_key_from_tab_name(self, tab_name): ...
    def get(self): ...
    AddRow: Any
    FindKeyFromTabName: Any
    Get: Any
    Layout: Any

class Slider(Element):
    TKScale: Any
    Range: Any
    DefaultValue: Any
    Orientation: Any
    BorderWidth: Any
    Relief: Any
    Resolution: Any
    ChangeSubmits: Any
    Disabled: Any
    TickInterval: Any
    DisableNumericDisplay: Any
    TroughColor: Any
    def __init__(self, range=..., default_value: Any | None = ..., resolution: Any | None = ..., tick_interval: Any | None = ..., orientation: Any | None = ..., disable_number_display: bool = ..., border_width: Any | None = ..., relief: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., disabled: bool = ..., size=..., s=..., font: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., trough_color: Any | None = ..., key: Any | None = ..., k: Any | None = ..., pad: Any | None = ..., tooltip: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, value: Any | None = ..., range=..., disabled: Any | None = ..., visible: Any | None = ...) -> None: ...
    Update: Any
Sl = Slider

class TkFixedFrame(tk.Frame):
    canvas: Any
    TKFrame: Any
    frame_id: Any
    def __init__(self, master, **kwargs) -> None: ...

class TkScrollableFrame(tk.Frame):
    vscrollbar: Any
    hscrollbar: Any
    canvas: Any
    TKFrame: Any
    frame_id: Any
    def __init__(self, master, vertical_only, **kwargs) -> None: ...
    def hookMouseWheel(self, e) -> None: ...
    def unhookMouseWheel(self, e) -> None: ...
    def resize_frame(self, e) -> None: ...
    def yscroll(self, event) -> None: ...
    def xscroll(self, event) -> None: ...
    def bind_mouse_scroll(self, parent, mode) -> None: ...
    def set_scrollregion(self, event: Any | None = ...) -> None: ...

class Column(Element):
    UseDictionary: bool
    ReturnValues: Any
    ReturnValuesList: Any
    ReturnValuesDictionary: Any
    DictionaryKeyCounter: int
    ParentWindow: Any
    ParentPanedWindow: Any
    Rows: Any
    TKFrame: Any
    TKColFrame: Any
    Scrollable: Any
    VerticalScrollOnly: Any
    RightClickMenu: Any
    ContainerElemementNumber: Any
    ElementJustification: Any
    Justification: Any
    VerticalAlignment: Any
    Grab: Any
    ExpandX: Any
    ExpandY: Any
    def __init__(self, layout, background_color: Any | None = ..., size=..., s=..., pad: Any | None = ..., scrollable: bool = ..., vertical_scroll_only: bool = ..., right_click_menu: Any | None = ..., key: Any | None = ..., k: Any | None = ..., visible: bool = ..., justification: Any | None = ..., element_justification: Any | None = ..., vertical_alignment: Any | None = ..., grab: Any | None = ..., expand_x: Any | None = ..., expand_y: Any | None = ..., metadata: Any | None = ...) -> None: ...
    def add_row(self, *args) -> None: ...
    def layout(self, rows): ...
    def update(self, visible: Any | None = ...) -> None: ...
    def contents_changed(self) -> None: ...
    AddRow: Any
    Layout: Any
    Update: Any
Col = Column

class Pane(Element):
    UseDictionary: bool
    ReturnValues: Any
    ReturnValuesList: Any
    ReturnValuesDictionary: Any
    DictionaryKeyCounter: int
    ParentWindow: Any
    Rows: Any
    TKFrame: Any
    PanedWindow: Any
    Orientation: Any
    PaneList: Any
    ShowHandle: Any
    Relief: Any
    HandleSize: Any
    BorderDepth: Any
    def __init__(self, pane_list, background_color: Any | None = ..., size=..., s=..., pad: Any | None = ..., orientation: str = ..., show_handle: bool = ..., relief=..., handle_size: Any | None = ..., border_width: Any | None = ..., key: Any | None = ..., k: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, visible: Any | None = ...) -> None: ...
    Update: Any

class TKCalendar(ttk.Frame):
    datetime: Any
    timedelta: Any
    format: Any
    close_when_chosen: Any
    def __init__(self, master: Any | None = ..., target_element: Any | None = ..., close_when_chosen: bool = ..., default_date=..., **kw) -> None: ...
    def __setitem__(self, item, value) -> None: ...
    def __getitem__(self, item): ...
    @property
    def selection(self): ...

class Menu(Element):
    BackgroundColor: Any
    TextColor: Any
    DisabledTextColor: Any
    MenuDefinition: Any
    Widget: Any
    MenuItemChosen: Any
    Tearoff: Any
    def __init__(self, menu_definition, background_color: Any | None = ..., text_color: Any | None = ..., disabled_text_color: Any | None = ..., size=..., s=..., tearoff: bool = ..., font: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    TKMenu: Any
    def update(self, menu_definition: Any | None = ..., visible: Any | None = ...) -> None: ...
    Update: Any
MenuBar = Menu
Menubar = Menu

class Table(Element):
    Values: Any
    ColumnHeadings: Any
    ColumnsToDisplay: Any
    ColumnWidths: Any
    MaxColumnWidth: Any
    DefaultColumnWidth: Any
    AutoSizeColumns: Any
    BackgroundColor: Any
    TextColor: Any
    HeaderTextColor: Any
    HeaderBackgroundColor: Any
    HeaderFont: Any
    Justification: Any
    InitialState: Any
    SelectMode: Any
    DisplayRowNumbers: Any
    NumRows: Any
    RowHeight: Any
    Widget: Any
    AlternatingRowColor: Any
    VerticalScrollOnly: Any
    HideVerticalScroll: Any
    SelectedRows: Any
    ChangeSubmits: Any
    BindReturnKey: Any
    StartingRowNumber: int
    RowHeaderText: str
    SelectedRowColors: Any
    RightClickMenu: Any
    RowColors: Any
    tree_ids: Any
    def __init__(self, values, headings: Any | None = ..., visible_column_map: Any | None = ..., col_widths: Any | None = ..., def_col_width: int = ..., auto_size_columns: bool = ..., max_col_width: int = ..., select_mode: Any | None = ..., display_row_numbers: bool = ..., num_rows: Any | None = ..., row_height: Any | None = ..., font: Any | None = ..., justification: str = ..., text_color: Any | None = ..., background_color: Any | None = ..., alternating_row_color: Any | None = ..., selected_row_colors=..., header_text_color: Any | None = ..., header_background_color: Any | None = ..., header_font: Any | None = ..., row_colors: Any | None = ..., vertical_scroll_only: bool = ..., hide_vertical_scroll: bool = ..., size=..., s=..., change_submits: bool = ..., enable_events: bool = ..., bind_return_key: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., tooltip: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    def update(self, values: Any | None = ..., num_rows: Any | None = ..., visible: Any | None = ..., select_rows: Any | None = ..., alternating_row_color: Any | None = ..., row_colors: Any | None = ...) -> None: ...
    def get(self): ...
    Update: Any
    Get: Any

class Tree(Element):
    image_dict: Any
    TreeData: Any
    ColumnHeadings: Any
    ColumnsToDisplay: Any
    ColumnWidths: Any
    MaxColumnWidth: Any
    DefaultColumnWidth: Any
    AutoSizeColumns: Any
    BackgroundColor: Any
    TextColor: Any
    HeaderTextColor: Any
    HeaderBackgroundColor: Any
    SelectedRowColors: Any
    HeaderFont: Any
    Justification: Any
    InitialState: Any
    SelectMode: Any
    ShowExpanded: Any
    NumRows: Any
    Col0Width: Any
    TKTreeview: Any
    element_frame: Any
    SelectedRows: Any
    ChangeSubmits: Any
    RightClickMenu: Any
    RowHeight: Any
    IconList: Any
    IdToKey: Any
    KeyToID: Any
    def __init__(self, data: Any | None = ..., headings: Any | None = ..., visible_column_map: Any | None = ..., col_widths: Any | None = ..., col0_width: int = ..., def_col_width: int = ..., auto_size_columns: bool = ..., max_col_width: int = ..., select_mode: Any | None = ..., show_expanded: bool = ..., change_submits: bool = ..., enable_events: bool = ..., font: Any | None = ..., justification: str = ..., text_color: Any | None = ..., background_color: Any | None = ..., selected_row_colors=..., header_text_color: Any | None = ..., header_background_color: Any | None = ..., header_font: Any | None = ..., num_rows: Any | None = ..., row_height: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., tooltip: Any | None = ..., right_click_menu: Any | None = ..., visible: bool = ..., metadata: Any | None = ...) -> None: ...
    photo: Any
    def add_treeview_data(self, node) -> None: ...
    def update(self, values: Any | None = ..., key: Any | None = ..., value: Any | None = ..., text: Any | None = ..., icon: Any | None = ..., visible: Any | None = ...): ...
    Update: Any

class TreeData:
    class Node:
        parent: Any
        children: Any
        key: Any
        text: Any
        values: Any
        icon: Any
        def __init__(self, parent, key, text, values, icon: Any | None = ...) -> None: ...
    tree_dict: Any
    root_node: Any
    def __init__(self) -> None: ...
    def insert(self, parent, key, text, values, icon: Any | None = ...) -> None: ...
    Insert: Any

class ErrorElement(Element):
    Key: Any
    def __init__(self, key: Any | None = ..., metadata: Any | None = ...) -> None: ...
    def update(self, silent_on_error: bool = ..., *args, **kwargs): ...
    def get(self): ...
    Get: Any
    Update: Any
Stretch = ErrorElement

class Window:
    NumOpenWindows: int
    hidden_master_root: tk.Tk
    AutoSizeText: Any
    AutoSizeButtons: Any
    Title: Any
    Rows: Any
    DefaultElementSize: Any
    DefaultButtonElementSize: Any
    Location: Any
    ButtonColor: Any
    BackgroundColor: Any
    ParentWindow: Any
    Font: Any
    RadioDict: Any
    BorderDepth: Any
    WindowIcon: Any
    AutoClose: Any
    NonBlocking: bool
    TKroot: Any
    TKrootDestroyed: bool
    CurrentlyRunningMainloop: bool
    FormRemainedOpen: bool
    TKAfterID: Any
    ProgressBarColor: Any
    AutoCloseDuration: Any
    RootNeedsDestroying: bool
    Shown: bool
    ReturnValues: Any
    ReturnValuesList: Any
    ReturnValuesDictionary: Any
    DictionaryKeyCounter: int
    LastButtonClicked: Any
    LastButtonClickedWasRealtime: bool
    UseDictionary: bool
    UseDefaultFocus: Any
    ReturnKeyboardEvents: Any
    LastKeyboardEvent: Any
    TextJustification: Any
    NoTitleBar: Any
    GrabAnywhere: Any
    KeepOnTop: Any
    ForceTopLevel: Any
    Resizable: Any
    Timeout: Any
    TimeoutKey: Any
    TimerCancelled: bool
    DisableClose: Any
    DisableMinimize: Any
    XFound: bool
    ElementPadding: Any
    RightClickMenu: Any
    Margins: Any
    ContainerElemementNumber: Any
    AllKeysDict: Any
    TransparentColor: Any
    UniqueKeyCounter: int
    DebuggerEnabled: Any
    WasClosed: bool
    ElementJustification: Any
    FocusSet: bool
    TtkTheme: Any
    UseTtkButtons: Any
    user_bind_dict: Any
    user_bind_event: Any
    modal: Any
    thread_queue: Any
    thread_lock: Any
    thread_timer: Any
    thread_strvar: Any
    read_closed_window_count: int
    config_last_size: Any
    config_last_location: Any
    starting_window_position: Any
    not_completed_initial_movement: bool
    config_count: int
    saw_00: bool
    maximized: bool
    right_click_menu_background_color: Any
    right_click_menu_text_color: Any
    right_click_menu_disabled_text_color: Any
    right_click_menu_font: Any
    right_click_menu_tearoff: Any
    auto_close_timer_needs_starting: bool
    finalize_in_progress: bool
    close_destroys_window: Any
    override_custom_titlebar: bool
    use_custom_titlebar: Any
    titlebar_background_color: Any
    titlebar_text_color: Any
    titlebar_font: Any
    titlebar_icon: Any
    right_click_menu_selected_colors: Any
    def __init__(self, title, layout: Any | None = ..., default_element_size=..., default_button_element_size=..., auto_size_text: Any | None = ..., auto_size_buttons: Any | None = ..., location=..., size=..., element_padding: Any | None = ..., margins=..., button_color: Any | None = ..., font: Any | None = ..., progress_bar_color=..., background_color: Any | None = ..., border_depth: Any | None = ..., auto_close: bool = ..., auto_close_duration=..., icon: Any | None = ..., force_toplevel: bool = ..., alpha_channel: int = ..., return_keyboard_events: bool = ..., use_default_focus: bool = ..., text_justification: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., resizable: bool = ..., disable_close: bool = ..., disable_minimize: bool = ..., right_click_menu: Any | None = ..., transparent_color: Any | None = ..., debugger_enabled: bool = ..., right_click_menu_background_color: Any | None = ..., right_click_menu_text_color: Any | None = ..., right_click_menu_disabled_text_color: Any | None = ..., right_click_menu_selected_colors=..., right_click_menu_font: Any | None = ..., right_click_menu_tearoff: bool = ..., finalize: bool = ..., element_justification: str = ..., ttk_theme: Any | None = ..., use_ttk_buttons: Any | None = ..., modal: bool = ..., enable_close_attempted_event: bool = ..., titlebar_background_color: Any | None = ..., titlebar_text_color: Any | None = ..., titlebar_font: Any | None = ..., titlebar_icon: Any | None = ..., use_custom_titlebar: Any | None = ..., metadata: Any | None = ...) -> None: ...
    @classmethod
    def get_screen_size(self): ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, value) -> None: ...
    def add_row(self, *args) -> None: ...
    def add_rows(self, rows) -> None: ...
    def layout(self, rows): ...
    def extend_layout(self, container, rows): ...
    def LayoutAndRead(self, rows, non_blocking: bool = ...) -> None: ...
    def LayoutAndShow(self, rows) -> None: ...
    def set_icon(self, icon: Any | None = ..., pngbase64: Any | None = ...) -> None: ...
    def read(self, timeout: Any | None = ..., timeout_key=..., close: bool = ...): ...
    def finalize(self): ...
    def refresh(self): ...
    def fill(self, values_dict): ...
    def find_element(self, key, silent_on_error: bool = ...): ...
    Element: Any
    Find: Any
    Elem: Any
    def find_element_with_focus(self): ...
    def element_list(self): ...
    def save_to_disk(self, filename) -> None: ...
    def load_from_disk(self, filename) -> None: ...
    def get_screen_dimensions(self): ...
    def move(self, x, y) -> None: ...
    def minimize(self) -> None: ...
    def maximize(self) -> None: ...
    def normal(self) -> None: ...
    def close(self) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...
    def hide(self) -> None: ...
    def un_hide(self) -> None: ...
    def disappear(self) -> None: ...
    def reappear(self) -> None: ...
    def set_alpha(self, alpha) -> None: ...
    @property
    def alpha_channel(self): ...
    @alpha_channel.setter
    def alpha_channel(self, alpha) -> None: ...
    def bring_to_front(self) -> None: ...
    def send_to_back(self) -> None: ...
    def current_location(self): ...
    @property
    def size(self): ...
    @size.setter
    def size(self, size) -> None: ...
    def set_min_size(self, size) -> None: ...
    def visibility_changed(self) -> None: ...
    def set_transparent_color(self, color) -> None: ...
    def grab_any_where_on(self) -> None: ...
    def grab_any_where_off(self) -> None: ...
    def bind(self, bind_string, key): ...
    def enable_debugger(self) -> None: ...
    def disable_debugger(self) -> None: ...
    def set_title(self, title) -> None: ...
    def make_modal(self) -> None: ...
    def force_focus(self) -> None: ...
    def was_closed(self): ...
    def set_cursor(self, cursor) -> None: ...
    def ding(self, display_number: int = ...) -> None: ...
    def write_event_value(self, key, value) -> None: ...
    @property
    def key_dict(self): ...
    def __getitem__(self, key): ...
    def __call__(self, *args, **kwargs): ...
    AddRow: Any
    AddRows: Any
    AlphaChannel: Any
    BringToFront: Any
    Close: Any
    CurrentLocation: Any
    Disable: Any
    DisableDebugger: Any
    Disappear: Any
    Enable: Any
    EnableDebugger: Any
    Fill: Any
    Finalize: Any
    FindElement: Any
    FindElementWithFocus: Any
    GetScreenDimensions: Any
    GrabAnyWhereOff: Any
    GrabAnyWhereOn: Any
    Hide: Any
    Layout: Any
    LoadFromDisk: Any
    Maximize: Any
    Minimize: Any
    Move: Any
    Normal: Any
    Read: Any
    Reappear: Any
    Refresh: Any
    SaveToDisk: Any
    SendToBack: Any
    SetAlpha: Any
    SetIcon: Any
    SetTransparentColor: Any
    Size: Any
    UnHide: Any
    VisibilityChanged: Any
    CloseNonBlocking: Any
    CloseNonBlockingForm: Any
FlexForm = Window

def read_all_windows(timeout: Any | None = ..., timeout_key=...): ...

SYSTEM_TRAY_WIN_MARGINS: Any
SYSTEM_TRAY_MESSAGE_MAX_LINE_LENGTH: int
SYSTEM_TRAY_MESSAGE_WIN_COLOR: str
SYSTEM_TRAY_MESSAGE_TEXT_COLOR: str
SYSTEM_TRAY_MESSAGE_DISPLAY_DURATION_IN_MILLISECONDS: int
SYSTEM_TRAY_MESSAGE_FADE_IN_DURATION: int
EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED: str
EVENT_SYSTEM_TRAY_ICON_ACTIVATED: str
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED: str
SYSTEM_TRAY_MESSAGE_ICON_INFORMATION: Any
SYSTEM_TRAY_MESSAGE_ICON_WARNING: Any
SYSTEM_TRAY_MESSAGE_ICON_CRITICAL: Any
SYSTEM_TRAY_MESSAGE_ICON_NOICON: Any

class SystemTray:
    Menu: Any
    TrayIcon: Any
    Shown: bool
    MenuItemChosen: Any
    last_message_event: Any
    window: Any
    def __init__(self, menu: Any | None = ..., filename: Any | None = ..., data: Any | None = ..., data_base64: Any | None = ..., tooltip: Any | None = ..., metadata: Any | None = ...) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, value) -> None: ...
    def read(self, timeout: Any | None = ...): ...
    def hide(self) -> None: ...
    def un_hide(self) -> None: ...
    def show_message(self, title, message, filename: Any | None = ..., data: Any | None = ..., data_base64: Any | None = ..., messageicon: Any | None = ..., time=...): ...
    def close(self) -> None: ...
    def update(self, menu: Any | None = ..., tooltip: Any | None = ..., filename: Any | None = ..., data: Any | None = ..., data_base64: Any | None = ...) -> None: ...
    @classmethod
    def notify(cls, title, message, icon=..., display_duration_in_ms=..., fade_in_duration=..., alpha: float = ..., location: Any | None = ...): ...
    Close: Any
    Hide: Any
    Read: Any
    ShowMessage: Any
    UnHide: Any
    Update: Any

def Sizer(h_pixels: int = ..., v_pixels: int = ...): ...
def pin(elem, vertical_alignment: Any | None = ..., shrink: bool = ..., expand_x: Any | None = ..., expand_y: Any | None = ...): ...
def vtop(elem_or_row, expand_x: Any | None = ..., expand_y: Any | None = ...): ...
def vcenter(elem_or_row, expand_x: Any | None = ..., expand_y: Any | None = ...): ...
def vbottom(elem_or_row, expand_x: Any | None = ..., expand_y: Any | None = ...): ...
def Titlebar(title: str = ..., icon: Any | None = ..., text_color: Any | None = ..., background_color: Any | None = ..., font: Any | None = ..., key: Any | None = ..., k: Any | None = ...): ...
def MenubarCustom(menu_definition, disabled_text_color: Any | None = ..., bar_font: Any | None = ..., font: Any | None = ..., tearoff: bool = ..., pad: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., bar_background_color: Any | None = ..., bar_text_color: Any | None = ..., key: Any | None = ..., k: Any | None = ...): ...
def FolderBrowse(button_text: str = ..., target=..., initial_folder: Any | None = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., change_submits: bool = ..., enable_events: bool = ..., font: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def FileBrowse(button_text: str = ..., target=..., file_types=..., initial_folder: Any | None = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., font: Any | None = ..., disabled: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def FilesBrowse(button_text: str = ..., target=..., file_types=..., disabled: bool = ..., initial_folder: Any | None = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., font: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., files_delimiter=..., metadata: Any | None = ...): ...
def FileSaveAs(button_text: str = ..., target=..., file_types=..., initial_folder: Any | None = ..., default_extension: str = ..., disabled: bool = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., font: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def SaveAs(button_text: str = ..., target=..., file_types=..., initial_folder: Any | None = ..., default_extension: str = ..., disabled: bool = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., change_submits: bool = ..., enable_events: bool = ..., font: Any | None = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Save(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., bind_return_key: bool = ..., disabled: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Submit(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., bind_return_key: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Open(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., bind_return_key: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def OK(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., bind_return_key: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Ok(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., bind_return_key: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Cancel(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Quit(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Exit(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Yes(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def No(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., tooltip: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Help(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., font: Any | None = ..., tooltip: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def Debug(button_text: str = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., font: Any | None = ..., tooltip: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def SimpleButton(button_text, image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., border_width: Any | None = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., disabled: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def CloseButton(button_text, image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., border_width: Any | None = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., disabled: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
CButton = CloseButton

def ReadButton(button_text, image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., border_width: Any | None = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., font: Any | None = ..., bind_return_key: bool = ..., disabled: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
ReadFormButton = ReadButton
RButton = ReadFormButton

def RealtimeButton(button_text, image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., border_width: Any | None = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., font: Any | None = ..., disabled: bool = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def DummyButton(button_text, image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., border_width: Any | None = ..., tooltip: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., font: Any | None = ..., disabled: bool = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def CalendarButton(button_text, target=..., close_when_date_chosen: bool = ..., default_date_m_d_y=..., image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., tooltip: Any | None = ..., border_width: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., font: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., enable_events: Any | None = ..., key: Any | None = ..., k: Any | None = ..., locale: Any | None = ..., format: str = ..., begin_at_sunday_plus: int = ..., month_names: Any | None = ..., day_abbreviations: Any | None = ..., title: str = ..., no_titlebar: bool = ..., location=..., metadata: Any | None = ...): ...
def ColorChooserButton(button_text, target=..., image_filename: Any | None = ..., image_data: Any | None = ..., image_size=..., image_subsample: Any | None = ..., tooltip: Any | None = ..., border_width: Any | None = ..., size=..., s=..., auto_size_button: Any | None = ..., button_color: Any | None = ..., disabled: bool = ..., font: Any | None = ..., bind_return_key: bool = ..., focus: bool = ..., pad: Any | None = ..., key: Any | None = ..., k: Any | None = ..., metadata: Any | None = ...): ...
def button_color_to_tuple(color_tuple_or_string, default=...): ...
def AddToReturnDictionary(form, element, value) -> None: ...
def AddToReturnList(form, value) -> None: ...
def InitializeResults(form) -> None: ...
def DecodeRadioRowCol(RadValue): ...
def EncodeRadioRowCol(container, row, col): ...
def fill_form_with_values(window, values_dict) -> None: ...
def AddMenuItem(top_menu, sub_menu_info, element, is_sub_menu: bool = ..., skip: bool = ..., right_click_menu: bool = ...): ...

class VarHolder:
    canvas_holder: Any
    def __init__(self) -> None: ...

def PackFormIntoFrame(form, containing_frame, toplevel_form): ...
def StartupTK(window) -> None: ...
def convert_args_to_single_string(*args): ...

METER_REASON_CANCELLED: str
METER_REASON_CLOSED: str
METER_REASON_REACHED_MAX: str
METER_OK: bool
METER_STOPPED: bool

class QuickMeter:
    active_meters: Any
    exit_reasons: Any
    start_time: Any
    key: Any
    orientation: Any
    bar_color: Any
    size: Any
    grab_anywhere: Any
    button_color: Any
    border_width: Any
    no_titlebar: Any
    title: Any
    current_value: Any
    max_value: Any
    close_reason: Any
    window: Any
    def __init__(self, title, current_value, max_value, key, *args, orientation: str = ..., bar_color=..., button_color=..., size=..., border_width: Any | None = ..., grab_anywhere: bool = ..., no_titlebar: bool = ...) -> None: ...
    def BuildWindow(self, *args): ...
    def UpdateMeter(self, current_value, max_value, *args): ...
    stat_messages: Any
    def ComputeProgressStats(self): ...

def one_line_progress_meter(title, current_value, max_value, *args, key: str = ..., orientation: str = ..., bar_color=..., button_color: Any | None = ..., size=..., border_width: Any | None = ..., grab_anywhere: bool = ..., no_titlebar: bool = ...): ...
def one_line_progress_meter_cancel(key: str = ...) -> None: ...
def get_complimentary_hex(color): ...

class _DebugWin:
    debug_window: Any
    size: Any
    location: Any
    font: Any
    no_titlebar: Any
    no_button: Any
    grab_anywhere: Any
    keep_on_top: Any
    do_not_reroute_stdout: Any
    resizable: Any
    output_element: Any
    layout: Any
    window: Any
    def __init__(self, size=..., location=..., font: Any | None = ..., no_titlebar: bool = ..., no_button: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., do_not_reroute_stdout: bool = ..., resizable: bool = ...) -> None: ...
    def Print(self, *args, end: Any | None = ..., sep: Any | None = ..., text_color: Any | None = ..., background_color: Any | None = ..., erase_all: bool = ..., font: Any | None = ...) -> None: ...
    def Close(self) -> None: ...

def easy_print(*args, size=..., end: Any | None = ..., sep: Any | None = ..., location=..., font: Any | None = ..., no_titlebar: bool = ..., no_button: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., do_not_reroute_stdout: bool = ..., text_color: Any | None = ..., background_color: Any | None = ..., colors: Any | None = ..., c: Any | None = ..., erase_all: bool = ..., resizable: bool = ...) -> None: ...
def easy_print_close() -> None: ...

CPRINT_DESTINATION_WINDOW: Any
CPRINT_DESTINATION_MULTILINE_ELMENT_KEY: Any

def cprint_set_output_destination(window, multiline_key) -> None: ...
def cprint(*args, end: Any | None = ..., sep: str = ..., text_color: Any | None = ..., font: Any | None = ..., t: Any | None = ..., background_color: Any | None = ..., b: Any | None = ..., colors: Any | None = ..., c: Any | None = ..., window: Any | None = ..., key: Any | None = ..., justification: Any | None = ...) -> None: ...
def set_global_icon(icon) -> None: ...
def set_options(icon: Any | None = ..., button_color: Any | None = ..., element_size=..., button_element_size=..., margins=..., element_padding=..., auto_size_text: Any | None = ..., auto_size_buttons: Any | None = ..., font: Any | None = ..., border_width: Any | None = ..., slider_border_width: Any | None = ..., slider_relief: Any | None = ..., slider_orientation: Any | None = ..., autoclose_time: Any | None = ..., message_box_line_width: Any | None = ..., progress_meter_border_depth: Any | None = ..., progress_meter_style: Any | None = ..., progress_meter_relief: Any | None = ..., progress_meter_color: Any | None = ..., progress_meter_size: Any | None = ..., text_justification: Any | None = ..., background_color: Any | None = ..., element_background_color: Any | None = ..., text_element_background_color: Any | None = ..., input_elements_background_color: Any | None = ..., input_text_color: Any | None = ..., scrollbar_color: Any | None = ..., text_color: Any | None = ..., element_text_color: Any | None = ..., debug_win_size=..., window_location=..., error_button_color=..., tooltip_time: Any | None = ..., tooltip_font: Any | None = ..., use_ttk_buttons: Any | None = ..., ttk_theme: Any | None = ..., suppress_error_popups: Any | None = ..., suppress_raise_key_errors: Any | None = ..., suppress_key_guessing: Any | None = ..., enable_treeview_869_patch: Any | None = ..., enable_mac_notitlebar_patch: Any | None = ..., use_custom_titlebar: Any | None = ..., titlebar_background_color: Any | None = ..., titlebar_text_color: Any | None = ..., titlebar_font: Any | None = ..., titlebar_icon: Any | None = ..., user_settings_path: Any | None = ..., pysimplegui_settings_path: Any | None = ..., pysimplegui_settings_filename: Any | None = ...): ...

LOOK_AND_FEEL_TABLE: Any

def list_of_look_and_feel_values(): ...
def theme(new_theme: Any | None = ...): ...
def theme_background_color(color: Any | None = ...): ...

TRANSPARENT_BUTTON: Any

def theme_element_background_color(color: Any | None = ...): ...
def theme_text_color(color: Any | None = ...): ...
def theme_text_element_background_color(color: Any | None = ...): ...
def theme_input_background_color(color: Any | None = ...): ...
def theme_input_text_color(color: Any | None = ...): ...
def theme_button_color(color: Any | None = ...): ...
def theme_progress_bar_color(color: Any | None = ...): ...
def theme_slider_color(color: Any | None = ...): ...
def theme_border_width(border_width: Any | None = ...): ...
def theme_slider_border_width(border_width: Any | None = ...): ...
def theme_progress_bar_border_width(border_width: Any | None = ...): ...
def theme_element_text_color(color: Any | None = ...): ...
def theme_list(): ...
def theme_add_new(new_theme_name, new_theme_dict) -> None: ...
def theme_global(new_theme: Any | None = ...): ...
def theme_previewer(columns: int = ..., scrollable: bool = ..., scroll_area_size=..., search_string: Any | None = ..., location=...): ...
preview_all_look_and_feel_themes = theme_previewer

def theme_previewer_swatches() -> None: ...
def change_look_and_feel(index, force: bool = ...) -> None: ...
def obj_to_string_single_obj(obj): ...
def obj_to_string(obj, extra: str = ...): ...
def clipboard_set(new_value) -> None: ...
def clipboard_get(): ...
def popup(*args, title: Any | None = ..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., button_type=..., auto_close: bool = ..., auto_close_duration: Any | None = ..., custom_text=..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., any_key_closes: bool = ..., image: Any | None = ..., modal: bool = ...): ...
def MsgBox(*args) -> None: ...
def popup_scrolled(*args, title: Any | None = ..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., yes_no: bool = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., size=..., location=..., non_blocking: bool = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., font: Any | None = ..., image: Any | None = ..., icon: Any | None = ..., modal: bool = ..., no_sizegrip: bool = ...): ...
def popup_no_buttons(*args, title: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...) -> None: ...
def popup_non_blocking(*args, title: Any | None = ..., button_type=..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_quick(*args, title: Any | None = ..., button_type=..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: int = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_quick_message(*args, title: Any | None = ..., button_type=..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: int = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_no_titlebar(*args, title: Any | None = ..., button_type=..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_auto_close(*args, title: Any | None = ..., button_type=..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_error(*args, title: Any | None = ..., button_color=..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_cancel(*args, title: Any | None = ..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_ok(*args, title: Any | None = ..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_ok_cancel(*args, title: Any | None = ..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon=..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_yes_no(*args, title: Any | None = ..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., auto_close: bool = ..., auto_close_duration: Any | None = ..., non_blocking: bool = ..., icon: Any | None = ..., line_width: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_get_folder(message, title: Any | None = ..., default_path: str = ..., no_window: bool = ..., size=..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., icon: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., initial_folder: Any | None = ..., image: Any | None = ..., modal: bool = ..., history: bool = ..., history_setting_filename: Any | None = ...): ...
def popup_get_file(message, title: Any | None = ..., default_path: str = ..., default_extension: str = ..., save_as: bool = ..., multiple_files: bool = ..., file_types=..., no_window: bool = ..., size=..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., icon: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., initial_folder: Any | None = ..., image: Any | None = ..., files_delimiter=..., modal: bool = ..., history: bool = ..., history_setting_filename: Any | None = ...): ...
def popup_get_text(message, title: Any | None = ..., default_text: str = ..., password_char: str = ..., size=..., button_color: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., icon: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., image: Any | None = ..., modal: bool = ...): ...
def popup_get_date(start_mon: Any | None = ..., start_day: Any | None = ..., start_year: Any | None = ..., begin_at_sunday_plus: int = ..., no_titlebar: bool = ..., title: str = ..., keep_on_top: bool = ..., location=..., close_when_chosen: bool = ..., icon: Any | None = ..., locale: Any | None = ..., month_names: Any | None = ..., day_abbreviations: Any | None = ..., modal: bool = ...): ...
def popup_animated(image_source, message: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., alpha_channel: Any | None = ..., time_between_frames: int = ..., transparent_color: Any | None = ..., title: str = ..., icon: Any | None = ...): ...
def popup_notify(*args, title: str = ..., icon=..., display_duration_in_ms=..., fade_in_duration=..., alpha: float = ..., location: Any | None = ...): ...
def popup_menu(window, element, menu_def, title: Any | None = ..., location=...) -> None: ...
def popup_error_with_traceback(title, *messages) -> None: ...
def shell_with_animation(command, args: Any | None = ..., image_source=..., message: Any | None = ..., background_color: Any | None = ..., text_color: Any | None = ..., font: Any | None = ..., no_titlebar: bool = ..., grab_anywhere: bool = ..., keep_on_top: bool = ..., location=..., alpha_channel: Any | None = ..., time_between_frames: int = ..., transparent_color: Any | None = ...): ...

class UserSettings:
    path: Any
    filename: Any
    full_filename: Any
    dict: Any
    default_value: Any
    silent_on_error: Any
    def __init__(self, filename: Any | None = ..., path: Any | None = ..., silent_on_error: bool = ...) -> None: ...
    def set_default_value(self, default) -> None: ...
    def set_location(self, filename: Any | None = ..., path: Any | None = ...) -> None: ...
    def get_filename(self, filename: Any | None = ..., path: Any | None = ...): ...
    def save(self, filename: Any | None = ..., path: Any | None = ...): ...
    def load(self, filename: Any | None = ..., path: Any | None = ...): ...
    def delete_file(self, filename: Any | None = ..., path: Any | None = ...) -> None: ...
    def write_new_dictionary(self, settings_dict) -> None: ...
    def read(self): ...
    def exists(self, filename: Any | None = ..., path: Any | None = ...): ...
    def delete_entry(self, key) -> None: ...
    def set(self, key, value): ...
    def get(self, key, default: Any | None = ...): ...
    def get_dict(self): ...
    def __setitem__(self, item, value) -> None: ...
    def __getitem__(self, item): ...
    def __delitem__(self, item) -> None: ...

def user_settings_filename(filename: Any | None = ..., path: Any | None = ...): ...
def user_settings_delete_filename(filename: Any | None = ..., path: Any | None = ...) -> None: ...
def user_settings_set_entry(key, value) -> None: ...
def user_settings_delete_entry(key) -> None: ...
def user_settings_get_entry(key, default: Any | None = ...): ...
def user_settings_save(filename: Any | None = ..., path: Any | None = ...): ...
def user_settings_load(filename: Any | None = ..., path: Any | None = ...): ...
def user_settings_file_exists(filename: Any | None = ..., path: Any | None = ...): ...
def user_settings_write_new_dictionary(settings_dict) -> None: ...
def user_settings_silent_on_error(silent_on_error: bool = ...) -> None: ...
def user_settings(): ...
def execute_command_subprocess(command, *args, wait: bool = ..., cwd: Any | None = ..., pipe_output: bool = ...): ...
def execute_py_file(pyfile, parms: Any | None = ..., cwd: Any | None = ..., interpreter_command: Any | None = ..., wait: bool = ..., pipe_output: bool = ...): ...
def execute_py_get_interpreter(): ...
def execute_editor(file_to_edit, line_number: Any | None = ...): ...
def execute_get_results(subprocess_id, timeout: Any | None = ...): ...
def execute_subprocess_still_running(subprocess_id): ...
def execute_file_explorer(folder_to_open: str = ...): ...
def execute_find_callers_filename(): ...

red_x: bytes
COLOR_SCHEME: str
DEBUGGER_POPOUT_THEME: str
WIDTH_VARIABLES: int
WIDTH_RESULTS: int
WIDTH_WATCHER_VARIABLES: int
WIDTH_WATCHER_RESULTS: int
WIDTH_LOCALS: int
NUM_AUTO_WATCH: int
MAX_LINES_PER_RESULT_FLOATING: int
MAX_LINES_PER_RESULT_MAIN: int
POPOUT_WINDOW_FONT: str
DEBUGGER_VARIABLE_DETAILS_FONT: str

class _Debugger:
    debugger: Any
    watcher_window: Any
    popout_window: Any
    local_choices: Any
    myrc: str
    custom_watch: str
    locals: Any
    globals: Any
    popout_choices: Any
    def __init__(self) -> None: ...

def show_debugger_window(location=..., *args): ...
def show_debugger_popout_window(location=..., *args) -> None: ...
def get_versions(): ...

EMOJI_BASE64_FACEPALM: bytes
EMOJI_BASE64_FRUSTRATED: bytes
EMOJI_BASE64_NOTUNDERSTANDING: bytes
EMOJI_BASE64_PONDER: bytes
EMOJI_BASE64_SAD: bytes
EMOJI_BASE64_SKEPTICAL: bytes
EMOJI_BASE64_THINK: bytes
EMOJI_BASE64_DREAMING: bytes
EMOJI_BASE64_WEARY: bytes
EMOJI_BASE64_YIKES: bytes
EMOJI_BASE64_HAPPY_GASP: bytes
EMOJI_BASE64_HAPPY_IDEA: bytes
EMOJI_BASE64_HAPPY_JOY: bytes
EMOJI_BASE64_HAPPY_LAUGH: bytes
EMOJI_BASE64_HAPPY_STARE: bytes
ICON_BUY_ME_A_COFFEE: bytes
EMOJI_BASE64_HAPPY_RELIEF: bytes
EMOJI_BASE64_HAPPY_BIG_SMILE: bytes
EMOJI_BASE64_HAPPY_CONTENT: bytes
EMOJI_BASE64_HAPPY_HEARTS: bytes
EMOJI_BASE64_HAPPY_THUMBS_UP: bytes
EMOJI_BASE64_HAPPY_WINK: bytes
EMOJI_BASE64_HAPPY_LIST: Any
EMOJI_BASE64_SAD_LIST: Any
EMOJI_BASE64_LIST: Any

def main_open_github_issue() -> None: ...
def main_get_debug_data(suppress_popup: bool = ...): ...
def main_global_pysimplegui_settings_erase() -> None: ...
def main_global_pysimplegui_settings(): ...
def main_sdk_help(): ...
def main() -> None: ...
ChangeLookAndFeel = change_look_and_feel
ConvertArgsToSingleString = convert_args_to_single_string
EasyPrint = easy_print
Print = easy_print
eprint = easy_print
sgprint = easy_print
PrintClose = easy_print_close
sgprint_close = easy_print_close
EasyPrintClose = easy_print_close
FillFormWithValues = fill_form_with_values
GetComplimentaryHex = get_complimentary_hex
ListOfLookAndFeelValues = list_of_look_and_feel_values
ObjToString = obj_to_string
ObjToStringSingleObj = obj_to_string_single_obj
OneLineProgressMeter = one_line_progress_meter
OneLineProgressMeterCancel = one_line_progress_meter_cancel
Popup = popup
PopupNoFrame = popup_no_titlebar
popup_no_frame = popup_no_titlebar
PopupNoBorder = popup_no_titlebar
popup_no_border = popup_no_titlebar
PopupAnnoying = popup_no_titlebar
popup_annoying = popup_no_titlebar
PopupAnimated = popup_animated
PopupAutoClose = popup_auto_close
PopupCancel = popup_cancel
PopupError = popup_error
PopupGetFile = popup_get_file
PopupGetFolder = popup_get_folder
PopupGetText = popup_get_text
PopupNoButtons = popup_no_buttons
PopupNoTitlebar = popup_no_titlebar
PopupNoWait = popup_non_blocking
popup_no_wait = popup_non_blocking
PopupNonBlocking = popup_non_blocking
PopupOK = popup_ok
PopupOKCancel = popup_ok_cancel
PopupQuick = popup_quick
PopupQuickMessage = popup_quick_message
PopupScrolled = popup_scrolled
PopupTimed = popup_auto_close
popup_timed = popup_auto_close
PopupYesNo = popup_yes_no
RGB = rgb
SetGlobalIcon = set_global_icon
SetOptions = set_options
sprint = popup_scrolled
ScrolledTextBox = popup_scrolled
TimerStart = timer_start
TimerStop = timer_stop
test = main
sdk_help = main_sdk_help
pysimplegui_user_settings: Any
