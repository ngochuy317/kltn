let slide_index = 0
let slide_play = true
let slides = document.querySelectorAll('.slide')

hideAllSlide = () => {
    slides.forEach(e => {
        e.classList.remove('active')
    })
}

showSlide = () => {
    hideAllSlide()
    slides[slide_index].classList.add('active')
}

nextSlide = () => slide_index = slide_index + 1 === slides.length ? 0 : slide_index + 1

prevSlide = () => slide_index = slide_index - 1 < 0 ? slides.length - 1 : slide_index - 1

// pause slide when hover slider

document.querySelector('.slider').addEventListener('mouseover', () => slide_play = false)

// enable slide when mouse leave out slider
document.querySelector('.slider').addEventListener('mouseleave', () => slide_play = true)

// slider controll

document.querySelector('.slide-next').addEventListener('click', () => {
    nextSlide()
    showSlide()
})

document.querySelector('.slide-prev').addEventListener('click', () => {
    prevSlide()
    showSlide()
})

showSlide()

// setInterval(() => {
//     if (!slide_play) return
//     nextSlide()
//     showSlide()
// }, 3000);

// render products

let products = [
    {
        name: '5 centimet trên giây',
        image1: './images/5-tren-giay.png',
        old_price: '50.000Đ',
        curr_price: '45.000Đ'
    },
    {
        name: 'Sách dạy nấu ăn',
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
        name: 'Ảo tưởng tình yêu',
        image1: './images/ao-tuong-tinh-yeu.png',
        old_price: '50.000Đ',
        curr_price: '45.000Đ'
    },
]

let product_list = document.querySelector('#latest-products')
let best_product_list = document.querySelector('#best-products')

products.forEach(e => {
    let prod = `

        <div class="col-3 col-md-6 col-sm-12">
            <div class="product-card">
                <div class="product-card-img">
                    <img style="height: 200px; width: 150px;" src="${e.image1}" alt="">
                  </div>
                <div class="product-card-info">
                    <div class="product-btn">
                    <a href="product-detail.html"><button class="btn-flat btn-hover btn-shop-now">Chi tiết</button></a>                                
                    <a href="shopping-cart.html"><button class="btn-flat btn-hover btn-cart-add">
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


