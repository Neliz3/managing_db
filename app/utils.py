import gspread
from db.models import Orders, Shop, Details, Products
import webbrowser


def exportOrders():
    gc = gspread.service_account()

    # Open a sheet from a spreadsheet in one go
    wks = gc.open("Report").sheet1

    wks.clear()

    # Update a range of cells using the top left corner address
    wks.update('A1', [["#", "Магазин", "Рік замовлення", "Товари (кількість)"]])
    count = 1
    for i in Orders.query.all():
        row = list()
        row.append(f"{i.id_order}")
        for j in Shop.query.all():
            if j.id_shop == i.id_shop:
                row.append(f"{j.name}")
        row.append(f"{i.year_order}")
        for det in Details.query.all():
            if i.id_order == det.id_order:
                for pr in Products.query.all():
                    if det.id_product == pr.id_product:
                        row.append(f"{pr.title} ({det.quantity})")
        count += 1
        wks.update(f'A{count}', [row])

    # Format the header
    wks.format('A1:D1', {'textFormat': {'bold': True}})

    spreadsheet_url = "https://docs.google.com/spreadsheets/d/%s" % wks.id
    webbrowser.open_new_tab(spreadsheet_url)
    return exportOrders


def exportProducts():
    gc_ = gspread.service_account()

    # Open a sheet from a spreadsheet in one go
    wks = gc_.open("Report").sheet1

    wks.clear()

    # Update a range of cells using the top left corner address
    wks.update('A1', [["Найменування", "Кількість"]])
    count = 1
    for i in Products.query.all():
        row = list()
        row.append(f"{i.title}")
        row.append(f"{i.amount}")

        count += 1
        wks.update(f'A{count}', [row])

    # Format the header
    wks.format('A1:B1', {'textFormat': {'bold': True}})

    spreadsheet_url = "https://docs.google.com/spreadsheets/d/%s" % wks.id
    webbrowser.open_new_tab(spreadsheet_url)

    return exportProducts
