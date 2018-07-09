#-*- coding:utf-8 -*-
#
# Copyright © 2016–2017 sthoo <sth201807@gmail.com>
#
# Support: Report an issue at https://github.com/sth2018/FastWordQuery/issues
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version; http://www.gnu.org/copyleft/gpl.html.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from .lang import _


VERSION = 'v1.0.9'


class Endpoint:
    repository = u'https://github.com/sth2018/FastWordQuery'
    feedback_issue = u'https://github.com/sth2018/FastWordQuery/issues'
    feedback_mail = u'sth201807@gmail.com'
    check_version = u'sth2018/FastWordQuery'
    user_guide = u'https://sth2018.github.io/FastWordQuery'
    version = VERSION


class Template:
    tmpl_about = u'''<b>{t0}</b><br/>{version}<br/><b>{t1}</b><br/>
        <a href="{url}">{url}</a><br/><b>{t2}</b><br/>
        <a href="{feedback0}">{feedback0}</a><br/>
        <a href="mailto:{feedback1}">{feedback1}</a>'''.format(
        t0=_('VERSION'), version=VERSION,
        t1=_('REPOSITORY'), url=Endpoint.repository,
        t2=_('FEEDBACK'), feedback0=Endpoint.feedback_issue, feedback1=Endpoint.feedback_mail)
    miss_css = u'MDX dictonary <b>{dict}</b> misses css file <b>{css}</b>. <br/>Please choose the file.'
