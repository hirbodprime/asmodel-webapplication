from django.http import HttpResponse

#...........................................................................................
#.
#.
#.
#..................// this function import Thousand seprator  //............................
#.
#.
#.
#...........................................................................................


def num_sep(a):
    import locale
    locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'
    #............................// for iran server host //..............................
    # import locale
    # locale.setlocale(locale.LC_ALL, 'en_US')
    # 'en_US'
    # ............................// for iran server host //..............................
    value = a
    # نسخه پایین در هاست به مشکل خورد و مقداری با جدا کننده به ما نشان نمیداد
    # بدین منظور ما از مورد پایین تر استفاده کردیم

    value = f'{value:n}'  # For Python ≥3.6

    # ............................// for iran server host //..............................

    # value = locale.format_string("%d", value, grouping=True)

    # ............................// for iran server host //..............................

    return value


#...........................................................................................
#.
#.
#.
#..................// this function import Thousand seprator  //............................
#.
#.
#.
#...........................................................................................


def re100(req, t_authority):
    import datetime
    from cart.models import Cart
    from HirMethods.Tamam import num_sep
    from factor.models import Factors, FacotrProduct
    from gateway.models import Transactions
    # .....................// important point //.........................
    # .
    #در اینجا ما از ویو gateway بخش verify مقداری که زرین پال برای ما
    # به عنوان شناسه درگاه ارسال کرده رو به عنوان یکی از ورودی های تابع دریافت میکنیم
    #در ورود دیگر یک رشته که شامل دیکشنری میشه که زرین پال برای ما ارسال کرده رو
    #در قالب یک پارامتر ورودی به نام req دریافت میکنیم تا بتونیم شماره پیکیری تراکنش ref_id
    # بگیرم برای ایجاد فاکتور
    # .
    # .....................// important point //.........................
    try:
        trans = Transactions.objects.get(authority=t_authority)
    except Transactions.DoesNotExist:
        return HttpResponse('Transaction Not Found')
    trans.state = 1
    trans.payment_date = datetime.datetime.now()
    # شماره تراکنش که به واسته اون و کاربر، ما فاکتور رو ایجاد میکنیم
    trans.ref_id = req.json()['data']['ref_id']
    trans.save()

    c = Cart.objects.filter(id_user=trans.user)

    # .........................//    شروع ایجاد فاکتور برای کاربر     //..................

    user_factor = Factors()
    # کاربری که تراکنش رو انجام داده
    user_factor.id_user = trans.user
    user_factor.payment_date = datetime.datetime.now()
    # کد پرداخت موفق برابر 1
    user_factor.state = 1
    user_factor.ref_id = req.json()['data']['ref_id']
    user_factor.creat_date = datetime.datetime.now()
    user_factor.save()
    # قیمت نهایی پس از وارد کردن محصولات در فاکتور ، در پایین وارد میشه

    # .........................//    پایان ایجاد فاکتور برای کاربر     //..................

    # .............................//  important point //...................................
    # .
    #  در اینجا ما باید یک رشته از فاکتور اصلی کاربر برای ساخت فکتور محصولات نیاز داریم
    # و برای بدست آوردن رشته مورد نظر هم از رشته کاربر استفاده می کنیم و هم از کد ref_id
    # چون یک کاربر ممکنه چندین فاکتور داشته باشه به
    # همین دلیل ما برای دریافت رشته مورد نظر هم از trans.user و هم ref_id استفاده کردیم
    # .
    # ............................//  important point //....................................

    user_factor = Factors.objects.get(ref_id=req.json()['data']['ref_id'], id_user=trans.user)
    pro_list = []
    gheymat = total_price = 0
    for i in c:
        # در اینجا چون کاربر هزینه محصول رو پرداخت کرده ، ما از قیمت واحدی (unit_price) که در سبد خرید
        # ثبت شده استفاده میکنیم

        show_price = num_sep(i.unit_price)
        #  این i.total_price قیمت کل هر محصول هستش
        show_total = num_sep(i.total_price)

        # اطلاعات ریز محصولات در por_list قرار دادیم

        pro_list.append([i.id_product.name, i.count, show_price, show_total, i.id_product.id,
                         i.id_product.category.name])

        # در اینجا قیمت کل هر محصول رو باهم جمع میکنیم تا قیمت نهایی بدس بیاد

        total_price += i.total_price

        # .........................//    شروع ایجاد فاکتور برای محصولات     //..................

        prod_factors = FacotrProduct()
        prod_factors.id_factor = user_factor
        # موارد id_product ,count ,unit_price ,total_price  رو از سبد خرید دریافت کردیم
        prod_factors.id_product = i.id_product
        prod_factors.count = i.count
        prod_factors.unit_price = i.unit_price
        prod_factors.total_price = i.total_price
        prod_factors.save()

    # متغییر gheymat مقداری عددی قیمت نهایی رو به قالب میفرسته
    # تا اگر جایی لازم بودم ازش استفاده بشه

    gheymat = total_price
    user_factor.total_price = gheymat
    user_factor.save()
    # متغییر total_price قیمت نهایی با جدا کننده رو  برای نمایش در فاکتور ارسال میکنه

    total_price = num_sep(total_price)

    # .........................//  default response in zarin pal //..........................
    # .
    # return HttpResponse('Transaction success.\nRefID: ' + str(
    #     req.json()['data']['ref_id'] ))
    # .
    # .........................//  default response in zarin pal //..........................

    context = {
        "amount": trans.amount,
        "pro": pro_list,
        "total_price": total_price,
        "show_sabad": gheymat,
        "RefID": req.json()['data']['ref_id']
    }
    c.delete()
    return context