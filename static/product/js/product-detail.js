// $(document).ready(function() {
//     $('.bar span').hide();
//     $('#bar-five').animate({
//        width: '75%'}, 1000);
//     $('#bar-four').animate({
//        width: '35%'}, 1000);
//     $('#bar-three').animate({
//        width: '20%'}, 1000);
//     $('#bar-two').animate({
//        width: '15%'}, 1000);
//     $('#bar-one').animate({
//        width: '30%'}, 1000);
    
//     setTimeout(function() {
//       $('.bar span').fadeIn('slow');
//     }, 1000);
    
//   });
document.querySelectorAll('.product-img-item').forEach(e => {
    e.addEventListener('click', () => {
        let img = e.querySelector('img').getAttribute('src')
        document.querySelector('#product-img > img').setAttribute('src', img)
    })
})

// document.querySelector('#view-all-description').addEventListener('click', () => {
//     let content = document.querySelector('.product-detail-description-content')
//     content.classList.toggle('active')
//     document.querySelector('#view-all-description').innerHTML = content.classList.contains('active') ? 'view less' : 'view all'
// })

let products = [
    {
        name: '5 centimet trên giây',
        image1: './images/5-tren-giay.png',
        old_price: '50.000Đ',
        curr_price: '45.000Đ'
    },
    {
        name: 'Sách dạy nấu ăn',
        image1: './images/sach-day-nau-an-200-mon-an-truyen-thong.png',
        old_price: '100.000Đ',
        curr_price: '90.000Đ'
    },
    {
        name: 'Bản chất của dối trá',
        image1: './images/sach-tam-ly-hay-nen-doc.png',
        old_price: '45.000Đ',
        curr_price: '40.000Đ'
    },
    {
        name: 'Tiểu sử Steve Jobs',
        image1: './images/tieu-su-steve-jobs.png',
        old_price: '150.000Đ',
        curr_price: '140.000Đ'
    },
    {
        name: 'Trí tuệ xúc cảm',
        image1: './images/tri-tue-xuc-cam.png',
        old_price: '60.000Đ',
        curr_price: '55.000Đ'
    },
    {
        name: 'Kỳ án ánh trăng',
        image1: './images/ki-an-anh-trang.png',
        old_price: '80.000Đ',
        curr_price: '75.000Đ'
    },
    {
        name: 'Kỳ án ánh trăng',
        image1: './images/ki-an-anh-trang.png',
        old_price: '80.000Đ',
        curr_price: '75.000Đ'
    },
    {
        name: 'Ảo tưởng tình yêu',
        image1: './images/ao-tuong-tinh-yeu.png',
        old_price: '50.000Đ',
        curr_price: '45.000Đ'
    },
    {
        name: 'Kỳ án ánh trăng',
        image1: './images/ki-an-anh-trang.png',
        old_price: '80.000Đ',
        curr_price: '75.000Đ'
    },
    {
        name: 'Ảo tưởng tình yêu',
        image1: './images/ao-tuong-tinh-yeu.png',
        old_price: '50.000Đ',
        curr_price: '45.000Đ'
    },{
        name: 'Kỳ án ánh trăng',
        image1: './images/ki-an-anh-trang.png',
        old_price: '80.000Đ',
        curr_price: '75.000Đ'
    },
    {
        name: 'Ảo tưởng tình yêu',
        image1: './images/ao-tuong-tinh-yeu.png',
        old_price: '50.000Đ',
        curr_price: '45.000Đ'
    },
]

let product_list = document.querySelector('#related-products')

renderProducts = (products) => {
    products.forEach(e => {
        let prod = `
            <div class="col-4 col-md-6 col-sm-12">
                <div class="product-card">
                    <div class="product-card-img">
                        <img style="height: 200px; width: 150px; transform: translateX(-7rem);" src="${e.image1}" alt="">
                    </div>
                    <div class="product-card-info">
                        <div class="product-btn">
                        <a href=""><button class="btn-flat btn-hover btn-shop-now">Chi tiết</button></a>                                
                        <a href=""><button class="btn-flat btn-hover btn-cart-add">
                            <i class='bx bxs-cart-add'></i>
                        </button>
                        </a>
                        </div>
                        <div class="product-card-name">
                            ${e.name}
                        </div>
                        <div class="product-card-price">
                            <span><del>${e.old_price}</del></span>
                            <span class="curr-price">${e.curr_price}</span>
                        </div>
                    </div>
                </div>
            </div>
        `
        product_list.insertAdjacentHTML("beforeend", prod)
    })
}

renderProducts(products)