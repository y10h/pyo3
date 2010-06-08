{% meta %}
    tags: [byteflow,  cyrax, jekyll]
    title: Генераторы статических блогов
{% endmeta %}

{% mark body %}{% filter markdown %}
Я давно присматриваюсь к блог-движкам, которые генерируют статический контент. До старта в 2006 я пробовал [thingamablog](http://www.thingamablog.com/), при переезде на pyobject.ru рассматривал [PyBlosxom](http://pyblosxom.sourceforge.net/). Теперь я снова ищу альтернативу «тяжелому» Byteflow, и хорошо что выбор есть.

Я нашел 17 генераторов. Конечно, большинство из них пригодятся разве что создателю, но некоторые «очень даже ничего». 5 блог-движков попало в «финалисты»:  [Cyrax](http://pypi.python.org/pypi/cyrax), [Golbarg](http://github.com/Schnouki/Golbarg),  [Growl](http://github.com/xfire/growl), [Jekyll](http://github.com/mojombo/jekyll), [Lanyon](http://bitbucket.org/arthurk/lanyon/).

Для моих целей, наверное, лучше всего подойдет [Cyrax](http://pypi.python.org/pypi/cyrax), и дело не в том, что его автор — [Александр Соловьев](http://piranha.org.ua) :)

<!--more-->

Требования к движку у меня простые: быть не назойливым и давать возможность вмешиваться в процесс генерации сайта не форкая сам генератор.

Для пятерки «финалистов» я сделал примерно одинаковый [пример](http://github.com/j2a/pyo-sandbox/tree/master/static-blog-generators/), так чтобы немного почувствовать инструменты в живую.

#### Jekyll

[Jekyll](http://github.com/mojombo/jekyll) — это то, что вдохновляет почти всех авторов, так что я не смог пройти мимо.

Нормальный инструмент. Немного не понравились шаблоны внутри (YAML-заголовок, некоторые нюансы Liquid). У Jekyll громадное коммунити и [тонны примеров](http://wiki.github.com/mojombo/jekyll/sites) использования. Этот движок я рассматривал как запасной вариант.

#### Golbarg

[Golbarg](http://github.com/Schnouki/Golbarg) сильно похож на Jekyll по организации «исходников» блога. Шаблоны организованы хорошо, но адаптация «под себя» возможна только с форканием Golbarg, точки расширения не предусмотрены. Не понравилось, что кастомные страницы (т.е. не блог-посты, а отдельные страницы) не допускают несколько уровней вложенности. Также отсутствует встроенный веб-сервер (либо привязки к внешнему) для тестирования сгенерированного сайта, приходится использовать что-то своё (я, к примеру, использовал twisted.web2). [Пример использования](http://github.com/Schnouki/schnouki.net) — блог автора.


#### Growl

[Growl](http://github.com/xfire/growl) очень сырой. Много хардкода, очень базовый функционал, всё (и очень много) нужно дописывать руками. [Пример использования](github.com/xfire/downgrade) — блог автора.

#### Lanyon

[Lanyon](http://bitbucket.org/arthurk/lanyon/) весьма добротный инструмент. Мне не понравились вездесущие YAML-заголовки в шаблонах, но всё остальное не вызывало неудобств. Точек расширения нет, предусмотрена только кастомная обработка урлов, к слову, весьма удачная. Пример не очень работающий, потому что автор закрыл свой блог, тем не менее, что-то найти в [примере](http://bitbucket.org/arthurk/arthurkoziel.com/) можно.

#### Cyrax

[Cyrax](http://pypi.python.org/pypi/cyrax) оставил смешанное впечатление. Есть удачные моменты и хороший код, а в других местах — непонятный хардкод и странные решения. Создалось впечатление, что «ядро» было сделано вдумчиво, а сверху быстренько дописан «как получится» недостающий функционал. Есть некоторая многословность в описании постов, но описание последовательно и не вызывает дискомфорт. Меня подкупила возможность расширения, причем не хаками, а вполне штатно. Пример использование есть в дистрибутиве.

#### Массовка

Список всех претендентов:

 * [Blatter](http://bitbucket.org/jek/blatter)
 * [Chisel](http://github.com/dz/chisel)
 * [Cyblog](http://github.com/basus/cyblog)
 * [Dorian](http://bitbucket.org/dialtone/dorian)
 * [Firmant](http://firmant.org/)
 * [Furthermore](http://github.com/drsnyder/furthermore)
 * [Hyde](http://github.com/lakshmivyas/hyde)
 * [Poole](http://bitbucket.org/obensonne/poole)
 * [Qsgen](http://www.stackfoundry.com/other/qsgen/)
 * [Stango](http://github.com/akheron/stango)

Вне зачёта еще посмотрел вики, которые можно использовать в [блог-режиме](http://ikiwiki.info/examples/blog/):

 * [Markdoc](http://github.com/zacharyvoase/markdoc)
 * [Webber](http://gitorious.org/webber/webber)
{% endfilter %}{% endmark %}
