class InputMixin:
    """
    Input Domain https://chromedevtools.github.io/devtools-protocol/tot/Input
    """
    def dispatch_key_event(self, type, modifiers=0, timestamp=None, text="",
                            unmodified_text="", key_identifier="", code="", key="",
                            windows_virtual_key_code=0, native_virtual_key_code=0,
                            auto_repeat=False, is_keypad=False, isSystemKey=False,
                            location=0):
        """
        Dispatches a key event to the page.
        """
        args = {
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": type,
                "modifiers": modifiers,
                "timestamp": timestamp,
                "text": text,
                "unmodifiedText": unmodified_text,
                "keyIdentifier": key_identifier,
                "code": code,
                "key": key,
                "windowsVirtualKeyCode": windows_virtual_key_code,
                "nativeVirtualKeyCode": native_virtual_key_code,
                "autoRepeat": auto_repeat,
                "isKeypad": is_keypad,
                "isSystemKey": is_system_key,
                "location": location
            }
        }
        return self._send(args)

    def dispatch_mouse_event(self, type, x, y, modifiers=0,
                            timestamp=None, button="none", click_count=0, delta_x=0,
                            delta_y=0):
        """
        Dispatches a mouse event to the page.
        """
        args = {
            "method": "Input.dispatchMouseEvent",
            "params": {
                "type": type,
                "x": x,
                "y": y,
                "modifiers": modifiers,
                "timestamp": timestamp,
                "button": button,
                "clickCount": click_count,
                "deltaX": delta_x,
                "deltaY": delta_y,
            }
        }
        return self._send(args)

    def dispatch_touch_event(self, type, touch_points, modifiers=0,
                            timestamp=None):
        """
        Dispatches a touch event to the page.
        """
        args = {
            "method": "Input.dispatchTouchEvent",
            "params": {
                "type": type,
                "touchPoints": touch_points,
                "modifiers": modifiers,
                "timestamp": timestamp,
            }
        }
        return self._send(args)

    def emulate_touch_from_mouse_event(self, type, x, y, button, timestamp=None,
                                delta_x=0, delta_y=0, modifiers=0, click_count=0):
        """
        Emulates touch event from the mouse event parameters.
        """
        args = {
            "method": "Input.emulateTouchFromMouseEvent",
            "params": {
                "type": type,
                "x": x,
                "y": y,
                "button": button,
                "timestamp": timestamp,
                "deltaX": delta_x,
                "deltaY": delta_y,
                "modifiers": modifiers,
                "clickCount": click_count,
            }
        }
        return self._send(args)

    def set_ignore_input_events(self, ignore):
        """
        Ignores input events (useful while auditing page).
        """
        args = {
            "method": "Input.setIgnoreInputEvents",
            "params": {
                "ignore": ignore,
            }
        }
        return self._send(args)

    def synthesize_pinch_gesture(self, x, y, scale_factor, relative_speed=800,
                                gesture_source_type="default"):
        """
        Synthesizes a pinch gesture over a time period by issuing appropriate touch events.
        """
        args = {
            "method": "Input.synthesizePinchGesture",
            "params": {
                "x": x,
                "y": y,
                "scaleFactor": scale_factor,
                "relativeSpeed": relative_speed,
                "gestureSourceType": gesture_source_type,
            }
        }
        return self._send(args)

    def synthesize_scroll_gesture(self, x, y, x_distance, y_distance, x_overscroll=0,
                                y_overscroll=0, prevent_fling=True, speed=800,
                                gesture_source_type='default', repeat_count=0, repeat_delay_ms=250, interaction_marker_name=""):
        """
        Synthesizes a scroll gesture over a time period by issuing appropriate touch events.
        """
        args = {
            "method": "Input.synthesizeScrollGesture",
            "params": {
                "x": x,
                "y": y,
                "xDistance": x_distance,
                "yDistance": y_distance,
                "xOverscroll": x_overscroll,
                "yOverscroll": y_overscroll,
                "preventFling": prevent_fling,
                "speed": speed,
                "gestureSourceType": gesture_source_type,
                "repeatCount": repeat_count,
                "repeatDelayMs": repeat_delay_ms,
                "interactionMarkerName": interaction_marker_name
            }
        }
        return self._send(args)

    def synthesize_tap_gesture(self, x, y, duration=50, tap_count=0, gesture_source_type='default'):
        """
        Synthesizes a tap gesture over a time period by issuing appropriate touch events.
        """
        args = {
            "method": "Input.synthesizeTapGesture",
            "params": {
                "x": x,
                "y": y,
                "duration": duration,
                "tapCound": tap_count,
                "gestureSourceType": gesture_source_type,
            }
        }
        return self._send(args)
