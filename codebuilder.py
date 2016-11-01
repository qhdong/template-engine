# -*- coding: utf-8 -*-


class CodeBuilder(object):
    """Build source code conveniently"""

    def __init__(self, indent=0):
        self.code = []
        self.indent_level = indent

    def add_line(self, line):
        self.code.extend([" " * self.indent_level, line, "\n"])

    INDENT_STEP = 4

    def indent(self):
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        self.indent_level -= self.INDENT_STEP

    def add_section(self):
        """Add a section, a sub-CodeBuilder"""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def __str__(self):
        return "".join(str(c) for c in self.code)

    def get_globals(self):
        """执行代码，返回它定义的全局变量的词典"""
        assert self.indent_level == 0
        python_source = str(self)
        global_namespace = {}
        exec(python_source, global_namespace)
        return global_namespace