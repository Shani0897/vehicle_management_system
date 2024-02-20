'use strict';


class Search_Record {
    constructor(id_name) {
        this.id_name = id_name;
    }

    search() {
        $(this.id_name).on('keyup', function () {

            var searchTerm = $(this).val().toLowerCase();

            $('#table_box tbody tr').each(function () {

                var text = $(this).text().toLowerCase();

                $(this).toggle(text.indexOf(searchTerm) > -1);
            });
        });
    }
}


let vehicle_category = new Search_Record('#search-input');

vehicle_category.search();