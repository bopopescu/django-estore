$(document).ready(function () {
    function setPrice() {
        var price = $('.variation_select option:selected').attr("data-price");
        var sale_price = $('.variation_select option:selected').attr("data-sale-price");
        if (sale_price  != "None" || sale_price==null) {
            $("#price").html(sale_price + " " + "<small class='og-price'>" + price + "</small>");
        }
        else {
            $('#price').text(price);
        }
    }

    $(document).ready(function () {
        //setPrice();
        $(".variation_select").change(function () {
            setPrice();
        })
    });
});