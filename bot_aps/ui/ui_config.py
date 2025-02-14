from PyQt5.QtGui import QPalette, QColor, QFont

def apply_dark_theme(widget):
    """Nustatome tamsią temą visam UI."""
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, QColor(200, 200, 200))
    palette.setColor(QPalette.Base, QColor(50, 50, 50))
    palette.setColor(QPalette.Text, QColor(220, 220, 220))
    widget.setPalette(palette)

def style_input_field(input_field):
    """Nustatome įvesties lauko stilių."""
    input_field.setFont(QFont("Arial", 16))
    input_field.setStyleSheet(
        "background-color: #228B22; color: white; border-radius: 8px; padding: 10px;"
    )
    input_field.setMinimumHeight(50)

def style_send_button(send_button):
    """Nustatome `Send` mygtuko stilių."""
    send_button.setFont(QFont("Arial", 16))
    send_button.setStyleSheet(
        "background-color: #B22222; color: white; border: 2px solid red; border-radius: 8px; padding: 10px;"
    )
    send_button.setMinimumHeight(50)
