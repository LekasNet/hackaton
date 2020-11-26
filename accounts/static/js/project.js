function init() {
    var x_b = document.querySelector('.block').getAttribute('data-attr-x_b');
    var y_b = document.querySelector('.block2').getAttribute('data-attr-y_b');
    var x_a = document.querySelector('.block3').getAttribute('data-attr-x_a');
    var y_a = document.querySelector('.block4').getAttribute('data-attr-y_a');
    var pointA = [x_a, y_a], 
        pointB = [x_b, y_b],
        /**
         * Создаем мультимаршрут.
         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/multiRouter.MultiRoute.xml
         */
        multiRoute = new ymaps.multiRouter.MultiRoute({
            referencePoints: [
                pointA,
                pointB
            ],
            params: {
                //Тип маршрутизации - пешеходная маршрутизация.
                routingMode: 'pedestrian'
            }
        }, {
            // Автоматически устанавливать границы карты так, чтобы маршрут был виден целиком.
            boundsAutoApply: true
        });

    // Создаем кнопку.
    var changePointsButton = new ymaps.control.Button({
        data: {content: "Поменять местами точки А и В"},
        options: {selectOnClick: true}
    });

    // Объявляем обработчики для кнопки.
    changePointsButton.events.add('select', function () {
        multiRoute.model.setReferencePoints([pointB, pointA]);
    });

    changePointsButton.events.add('deselect', function () {
        multiRoute.model.setReferencePoints([pointA, pointB]);
    });

    // Создаем карту с добавленной на нее кнопкой.
    var myMap = new ymaps.Map('map', {
        center: [x_a, y_a],
        zoom: 12,
    }, {
        buttonMaxWidth: 300
    });
    
    // Добавляем мультимаршрут на карту.
    myMap.geoObjects.add(multiRoute);
}

ymaps.ready(init);