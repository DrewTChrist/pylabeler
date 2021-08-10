from PyQt5.Qsci import QsciScintilla, QsciLexerHTML
from PyQt5.QtGui import QFont, QColor


class HtmlEditor(QsciScintilla):

    def __init__(self, parent):
        super(HtmlEditor, self).__init__(parent)
        self.setObjectName('htmlEditor')
        editor_font = QFont()
        editor_font.setFamily('Courier')
        editor_font.setFixedPitch(True)
        editor_font.setPointSize(16)
        lexer = QsciLexerHTML()
        lexer.setFont(editor_font)
        lexer.setParent(parent)
        self.setMarginsFont(editor_font)
        self.setLexer(lexer)
        self.setMarginLineNumbers(0, True)
        self.setMarginWidth(0, self.fontMetrics().width('000') + 20)
        self.setTabWidth(4)
        self.setIndentationsUseTabs(False)
        self.setAutoIndent(True)
        #self.SendScintilla(self.SCI_STYLESETBACK, self.STYLE_DEFAULT, QColor(255, 0, 0))

