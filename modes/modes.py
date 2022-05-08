from talon import Context, Module, app, actions, speech_system, scope

mod = Module()

modes = {
    "admin": "enable extra administration commands terminal (docker, etc)",
    "debug": "a way to force debugger commands to be loaded",
    "gdb": "a way to force gdb commands to be loaded",
    "ida": "a way to force ida commands to be loaded",
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
    "windbg": "a way to force windbg commands to be loaded",
}

for key, value in modes.items():
    mod.mode(key, value)


@mod.action_class
class Actions:
    def talon_mode():
        """For windows and Mac with Dragon, enables Talon commands and Dragon's command mode."""
        actions.speech.enable()
        actions.user.microphone_preferred()
        engine = speech_system.engine.name
        # app.notify(engine)
        if "dragon" in engine:
            if app.platform == "mac":
                actions.user.engine_sleep()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("switch to command mode")
        else:
            actions.mode.disable("sleep")
            actions.mode.disable("dictation")
            actions.mode.enable("command")
            actions.user.code_clear_language_mode()

    def dragon_mode():
        """For windows and Mac with Dragon, disables Talon commands and exits Dragon's command mode"""
        engine = speech_system.engine.name
        # app.notify(engine)

        if "dragon" in engine:
            # app.notify("dragon mode")
            actions.speech.disable()
            if app.platform == "mac":
                actions.user.engine_wake()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("start normal mode")
        else:
            actions.mode.disable("sleep")
            actions.mode.enable("dictation")
            actions.mode.disable("command")
            actions.user.code_clear_language_mode()

    def wake_or_sleep():
        """toggles wake or sleep"""
        modes = scope.get("mode")
        # print(str(modes))
        if not actions.speech.enabled():
            actions.user.welcome_back()
            actions.user.microphone_preferred()
        else:
            actions.user.sleep_all()
            actions.speech.set_microphone("None")

    def welcome_back():
        """Enables all things"""
        actions.user.mouse_wake()
        actions.user.hud_enable()
        # user.history_enable()
        actions.user.talon_mode()
        actions.mode.enable("noise")

    def sleep_all():
        """Disables all things"""
        actions.user.switcher_hide_running()
        actions.user.hud_disable()
        # user.history_disable()
        actions.user.homophones_hide()
        actions.user.help_hide()
        actions.user.mouse_sleep()
        actions.speech.disable()
        actions.user.engine_sleep()
        actions.mode.disable("noise")
