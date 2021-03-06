function init() {
    var x = document.querySelector('.block').getAttribute('data-attr-x');
    var y = document.querySelector('.block2').getAttribute('data-attr-y');
    var pointA = [x, y], 
        pointB = "Москва, Красная площадь",
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
        center: [x, y],
        zoom: 12,
    }, {
        buttonMaxWidth: 300
    });
    
    // Добавляем мультимаршрут на карту.
    myMap.geoObjects.add(multiRoute);
}

ymaps.ready(init);