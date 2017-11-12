%include('header.tpl')
% for a in objeto:
<nav id="menu2" class="clearfix" role="navigation">
        <ul>
                <li>
                        <a href="/listarclase/{{a}}">{{a}}</a>
                </li>
        </ul>
</nav>
% end
%include('foot.tpl')
