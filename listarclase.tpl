%include('header.tpl')
% for i in objeto:
        <li><a href="/todosanimales2/{{i[0]}}">{{i[0]}}</a></li>
% end
%include('foot.tpl')
