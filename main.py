from nicegui import ui

data = [
    ["Сестра", "Моя младшая сестра Ульяна, родилась 29 Января 2013 года, любит помогать маме и убирается по дому, добрая и позитивная.", "https://masterpiecer-images.s3.yandex.net/2bd3b9e6331711ee83f66ee9ab557742:upscaled"],
    ["Я", "Это я - старший брат Андрей, я родился 7 февраля 2009 года, частенько зависаю в телефоне и помогаю по дому.", "https://i.pinimg.com/736x/95/1e/94/951e942f1cd72a36714c7e111f6d8839.jpg"],
    ["Мама", "Моя мама Антонина, родилась 27 апреля 1986 года, добрая и отзывчивая, всегда поможет в трудную минуту.", "https://masterpiecer-images.s3.yandex.net/c3bc39cf7f3111ee8e8c56181a0358a2:upscaled"],
    ["Папа", "Мой папа Дмитрий, родился 5 ноября 1979 года, часто помогает по дому, что-то чинит, добрый и отзывчивый.", "https://photo9.wambacdn.net/46/65/04/1781405664/2042346497_huge.jpg?hash=rnr8acXuYPk5w4F_aGyXoA&expires=64060578000&updated=1599924270"],
    ["Бабушка", "Моя бабушка Татьяна, родилась 21 октября 1952 года, часто готовит что-то вкусное, следит за порядком в доме, добрая и веселая.", "https://i01.fotocdn.net/s215/5f6c0824d20f75f8/gallery_xl/2915780818.jpg"],
    ["Дедушка", "Мой дедушка Александр, родился 7 октября 1955 года, любит ходить на рыбалку, добрый и всегда помогает нам.", "https://masterpiecer-images.s3.yandex.net/5fe6228168fe22f:upscaled"]
]

def mouse_click(e, t):
     ui.notify(e.type + " " + str(t))
     print(e.type, t)
     ui.navigate.to(f"/{t}")

@ui.page("/")
async def index():
    ui.page_title("Моя Семья")

    with ui.header().classes('bg-gray-900 text-white rounded-b-lg shadow-lg border border-white/10').style("text-align: center;"):
        ui.label('Моя Семья').classes('text-white text-5xl font-extrabold').style("text-align: center;")


    with ui.element('div').style('position: relative; display: inline; margin-bottom: 10vh'):
        with ui.element('div').style('position: relative; display: inline-block; margin-left: 30px;').classes('bg-gray-900 rounded-lg border-2 border-white p-4') as image_container:
            im = ui.interactive_image(data[0][2], on_mouse=lambda e: mouse_click(e,0), events=["mousedown"]).classes('w-32 h-32 object-cover rounded-xl shadow-lg border border-white/10').style("left: center")
            ui.label(data[0][0]).style("font-size:25px; text-align: center;")

        with ui.element('div').style('position: relative; display: inline-block; margin-left: 30px;').classes('bg-gray-900 rounded-lg border-2 border-white p-4') as image_container:
            im = ui.interactive_image(data[1][2], on_mouse=lambda e: mouse_click(e, 1), events=["mousedown"]).classes('w-32 h-32 object-cover rounded-xl shadow-lg border border-white/10').style("left: center")
            ui.label(data[1][0]).style("font-size:25px; text-align: center;")

    with ui.element('div').style('position: relative; display: inline; margin-bottom: 10vh'):
        with ui.element('div').style('position: relative; display: inline-block; margin-left: 30px;').classes('bg-gray-900 rounded-lg border-2 border-white p-4') as image_container:
            im = ui.interactive_image(data[2][2], on_mouse=lambda e: mouse_click(e, 2), events=["mousedown"]).classes('w-32 h-32 object-cover rounded-xl shadow-lg border border-white/10').style("left: center")
            ui.label(data[2][0]).style("font-size:25px; text-align: center;")

        with ui.element('div').style('position: relative; display: inline-block; margin-left: 30px;').classes('bg-gray-900 rounded-lg border-2 border-white p-4') as image_container:
            im = ui.interactive_image(data[3][2], on_mouse=lambda e: mouse_click(e, 3), events=["mousedown"]).classes('w-32 h-32 object-cover rounded-xl shadow-lg border border-white/10').style("left: center")
            ui.label(data[3][0]).style("font-size:25px; text-align: center;")


    with ui.element('div').style('position: relative; display: inline; margin-bottom: 10vh'):
        with ui.element('div').style('position: relative; display: inline-block; margin-left: 30px;').classes('bg-gray-900 rounded-lg border-2 border-white p-4') as image_container:
            im = ui.interactive_image(data[4][2], on_mouse=lambda e: mouse_click(e, 4), events=["mousedown"]).classes('w-32 h-32 object-cover rounded-xl shadow-lg border border-white/10').style("left: center")
            ui.label(data[4][0]).style("font-size:25px; text-align: center;")

        with ui.element('div').style('position: relative; display: inline-block; margin-left: 30px;').classes('bg-gray-900 rounded-lg border-2 border-white p-4') as image_container:
            im = ui.interactive_image(data[5][2], on_mouse=lambda e: mouse_click(e, 5), events=["mousedown"]).classes('w-32 h-32 object-cover rounded-xl shadow-lg border border-white/10').style("left: center")
            ui.label(data[5][0]).style("font-size:25px; text-align: center;")

@ui.page("/{val}")
async def desription(val):
    with ui.element("div").style("display: flex; justify-content: center; align-items: center"):
        with ui.element('div').style('position: relative; display: inline-block; min-width: 95vw;').classes('bg-gray-900 rounded-lg border-2 border-white p-10') as image_container:
            ui.image(data[int(val)][2]).classes('w-60 h-60')
            ui.label(" ").style("font-size:45px").classes("font-bold")
            ui.label(data[int(val)][0]).style("font-size:45px").classes("font-bold")
            ui.label(" ").style("font-size:45px").classes("font-bold")
            ui.label(data[int(val)][1]).style("font-size:25px")
        

ui.run(dark=True, port=5678, host="0.0.0.0", storage_secret="hui123123", ssl_certfile="/etc/letsencrypt/live/s219035.foxcdn.net/fullchain.pem", ssl_keyfile="/etc/letsencrypt/live/s219035.foxcdn.net/privkey.pem")
