'use strict';

window.jsPDF = window.jspdf.jsPDF;


/* SIDE____________BAR_____________OFFCANVAS_____________________MENU */

let sidebar = document.querySelector(".sidebar");


let offcanvas = () => {
    sidebar.classList.toggle("open");
}

// SEARCH____________________________RECORD____________________ON_________________PAGE


class Search_Record {
    constructor(id_name) {
        this.id_name = id_name;
    }

    search(id_table) {
        $(this.id_name).on('keyup', function () {

            var searchTerm = $(this).val().toLowerCase();
            let found = false;

            $(id_table).each(function () {

                var text = $(this).text().toLowerCase();

                $(this).toggle(text.indexOf(searchTerm) > -1);
                if (text.indexOf(searchTerm) > -1) {
                    $(this).show();
                    found = true;
                } else {
                    $(this).hide();
                }
            });

            
            
        });
    }
}

let vehicle_category = new Search_Record('#search-input');

vehicle_category.search('.table_box tbody tr');

let vehicle_list_manage = new Search_Record('#search-vehicle-input')
vehicle_list_manage.search('.table_box tbody tr');

let Outgoing_Vehicle = new Search_Record('#search-outVehicle-input')
Outgoing_Vehicle.search('.table_box tbody tr')

let search_category = new Search_Record('#search_page_item');
    
search_category.search('.table_box tbody tr');


// GENERATE___________________________PDF_________________________DOCUMENT

function generatePdf(table_id) {
    // Create a new jsPDF instance
    var doc = new jsPDF();

    // Get the table element and convert it to a data array
    var table = document.getElementById(table_id);
    var tableData = [];

    for (var i = 0, row; row = table.rows[i]; i++) {
        var rowData = [];

        for (var j = 0, col; col = row.cells[j]; j++) {
            rowData.push(col.innerText);
        }

        tableData.push(rowData);
    }

    // Set the table column widths and row heights
    var columnWidths = [50, 20, 30];
    var rowHeight = 10;

    // Calculate the table height based on the number of rows and row height
    var tableHeight = (tableData.length + 1) * rowHeight;

    // Get the table header from the first row of the table
    var header = tableData.shift();

    // Define the style of the table header
    var headStyles = {
        /* fillColor: [245, 245, 245], */
        textColor: [0, 0, 0],
        fontSize: 12,
        fontStyle: 'bold',
        halign: 'center'
    };

    // Define the style of the table body
    var bodyStyles = {
        fillColor: [255, 255, 255],
        textColor: [0, 0, 0],
        fontSize: 10,
        halign: 'left',
        cellPadding: 3
    };

    var gridTheme = {
        tableLineColor: [189, 195, 199],
        tableLineWidth: 0.1,
        textColor: [51, 51, 51],
        fontStyle: 'normal',
        fontSize: 10,
        cellPadding: 5
    };
    // Add the table to the PDF document
    doc.autoTable({
        head: [header],
        body: tableData,
        startY: 20,
        margin: { top: 20 },
        columnWidth: columnWidths,
        rowHeight: rowHeight,
        styles: { overflow: 'linebreak' },
        headStyles: headStyles,
        bodyStyles: bodyStyles,
        theme: 'grid',
        themeStyle: gridTheme
    });

    // Get the PDF document as a data URL
    var pdfDataUri = doc.output('datauristring');

    // Open a new window and set its contents to an <iframe> element containing the PDF preview
    var previewWindow = window.open();
    previewWindow.document.write('<iframe src="' + pdfDataUri + '" width="100%" height="100%"></iframe>');
};



// CATEGORY_______________________TEMPLATE_____________________CODE________________START


/* CATEGORY__________ADD____________FORM__________DATA */

// Alert box function

let alert_function = (icon, text) => {
    swal({
        icon: icon,
        text: text,
        buttons: false,
        timer: 1600,
        closeOnClickOutside: false,
        className: 'swal-add-modal'
    });
}

try {

    let add_category_form = document.getElementById('addCategoryForm');

    add_category_form.addEventListener('submit', (e) => {
        e.preventDefault();

        fetch('/vehicle-category/add-category/', {
            method: 'POST',
            body: new FormData(add_category_form)

        })
            .then(response => response.json())
            .then((data) => {
                if (data.success) {
                    alert_function('success', data.success);
                    add_category_form.reset();
                    setTimeout(() => {
                        window.location.href = data.redirect_url;
                    }, 1600);
                    // console.log('success', data)

                } else if (data.duplicate_error) {

                    alert_function('warning', data.duplicate_error);
                    // console.log(data.duplicate_error)

                } else {
                    console.log(data.errors)
                }
            })
            .catch((error) => {
                console.log(error)
            })
    });

} catch (error) {
    console.log(error)
}


/* DELETE_______________CATEGORY_________________RECORD____________CODE */


function deleteItem(itemId) {
    // let categoryId = document.getElementById('category_id');
    swal({
        title: "Are you sure?",
        text: "you won't be able to revert this!",
        icon: 'warning',
        buttons: true,
        dangerMode: true,
        className: 'swal-delete-modal',
    })
        .then((willDelete) => {
            if (willDelete) {
                fetch(`/vehicle-category/delete-category/${itemId}/`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                })
                    .then(response => response.json())
                    .then(data => {
                        //console.log(data);
                        // console.log(data.objects)
                        const deletedItem = document.getElementById(`item-${itemId}`);
                        if (deletedItem) {
                            deletedItem.remove();
                        }

                        setTimeout(() => {
                            window.location.reload();
                            // window.location.href = data.redirect_url;
                        }, 1000);
                        // let objects = data.objects;
                        // for (var i = 0; i < objects.length; i++) {
                        //     var obj = objects[i];
                        //     console.log(obj)
                        //     $('#id_' + obj.id).text(obj.id);
                        // }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                swal({
                    title: 'deleted!',
                    text: 'deleted successfully.',
                    icon: "success",
                    className: 'swal-success-modal',
                })
            }
        });
}


// EDIT______________________CATEGORY___________________RECORD_______________CODE

let editRecord = (itemid) => {
    window.location.href = `/vehicle-category/update-vehicle-category/${itemid}`
}

try {

    let current_url = window.location.href;
    let parts = current_url.split('/')
    let id = parts[parts.length - 1]
    // console.log(id)

    let form = document.getElementById('category-edit-form');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        // console.log(itemid)
        fetch(`/vehicle-category/update-vehicle-category/${id}`, {
            method: 'POST',
            body: new FormData(form)
        })
            .then(response => response.json())
            .then(data => {
                // console.log(data)
                if (data.success) {
                    alert_function('success', data.success)
                    setTimeout(() => {
                        window.location.href = data.redirect_url;
                    }, 1600);
                } else {
                    console.log(data.errors)
                }
            })
            .catch(error => {
                console.log(error)
            })
    })
} catch (error) {
    console.log(error)
}


// VEHICLE________________MANAGE______________IN_____________TEMPLATE___________CODE_________START

// VEHICLE_______________________ADD________________FORM___________________CODE


try {

    let vehicle_form = document.getElementById('vehicleForm');

    vehicle_form.addEventListener('submit', (e) => {
        e.preventDefault();

        fetch('/vehicle-manageIn/add-vehicle/', {
            method: 'POST',
            body: new FormData(vehicle_form)
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {

                    alert_function('success', data.success);
                    vehicle_form.reset();
                    setTimeout(() => {
                        window.location.href = data.redirect_url;
                    }, 1600);
                    // console.log(data)
                } else {
                    console.log(data.errors)
                }
            })
            .catch(error => {
                console.log(error.errors)
            })

    })
} catch (error) {
    console.log(error)
}


try {

    let current_url = window.location.href;
    let parts = current_url.split('/')
    // console.log(parts)
    let id = parts[parts.length - 1]
    // console.log(id)
    let vehicle_form = document.getElementById('vehicleForm');

    vehicle_form.addEventListener('submit', (e) => {
        e.preventDefault();

        fetch(`/vehicle-manageIn/view-vehicle/${id}`, {
            method: 'POST',
            body: new FormData(vehicle_form)
        })
            .then(response => response.json())
            .then(data => {
                alert_function('success', data.success)
                setTimeout(() => {
                    window.location.href = data.redirect_url;
                }, 1600);
                // console.log(data)
            })
            .catch(error => {
                console.log(error)
            })
    })
} catch (error) {
    console.log(error)
}



// REPORTS_________________TEMPLATE__________________CODE_____________START

// SEARCH_____________FORM______________________CODE

try {
    let search_form = document.getElementById('form-search');

    search_form.addEventListener('submit', (e) => {
        e.preventDefault();

        fetch('/vehicle-report/reports/', {
            method: 'POST',
            body: new FormData(search_form)
        })
        .then(response => response.json())
        .then(data => {
            // console.log(data)
            let table_body = document.getElementById('tableBody');
            let response = data.data;
            let object = JSON.parse(response)
            // console.log(object)
            // console.log( data.data)
            object.forEach(records =>{
                // console.log(records.fields)
                table_body.innerHTML += `
                    <tr>
                    <td>${records.fields.parking_number}</td>
                    <td>${records.fields.owner_name}</td>
                    <td>${records.fields.registration_number}</td>
                    <td>vehicle in time ${records.fields.vehicle_in_time} / vehicle out time ${records.fields.vehicle_time_out}</td>
                    <td>${records.fields.vehicle_status}</td>
                    <td>0</td>
                    </tr>
                `
            })
            
              
            // console.log(table_body)           

        })
        .catch(error => {
            console.log(error)
        })
    })
} catch (error) {
    console.log(error)
}


