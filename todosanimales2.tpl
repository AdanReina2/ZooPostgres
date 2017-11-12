%include('header.tpl')
% for i in objeto:
	% if i[0] == info:
		<li>Nombre Cientifico de la especie: {{i[0]}}</li>
		<li>Esperanza de Vida: {{i[1]}}</li>
		<li>Descripción: {{i[2]}}</li>
		<li>Peligro de Extinción: {{i[3]}}</li>
		<li>Clase de Animal: {{i[4]}}</li>
	% end
% end
%include('foot.tpl')
