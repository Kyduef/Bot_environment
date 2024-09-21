import discord
from discord.ext import commands
import random
import os
# Discord bot intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot1
bot = commands.Bot(command_prefix='$', intents=intents)

# Waste reduction tips
waste_reduction_tips = [
    "Bawa tas belanja sendiri untuk mengurangi penggunaan plastik sekali pakai.",
    "Gunakan botol minum yang dapat diisi ulang untuk mengurangi limbah botol plastik.",
    "Pilah sampah organik dan non-organik agar lebih mudah diolah.",
    "Daur ulang plastik dan barang-barang elektronik di pusat daur ulang lokal.",
    "Gunakan produk yang dapat digunakan ulang, seperti sedotan stainless steel.",
    "Kurangi penggunaan kertas dengan beralih ke pembayaran digital atau e-receipt.",
    "Belanja produk yang memiliki kemasan minimal atau tanpa kemasan plastik.",
    "Berpartisipasi dalam program daur ulang dan pembersihan lingkungan di komunitas Anda.",
    "Kompos sampah organik untuk mengurangi limbah yang dibuang ke TPA.",
    "Beli barang-barang bekas untuk mengurangi produksi baru dan limbah."
]

# Energy-saving tips
energy_saving_tips = [
    "Matikan peralatan listrik yang tidak digunakan untuk menghemat energi.",
    "Gunakan lampu LED yang lebih hemat energi dibandingkan lampu biasa.",
    "Pakai AC dengan pengaturan suhu yang efisien (sekitar 24-26°C) untuk menghemat energi.",
    "Gunakan alat listrik dengan label energi yang lebih efisien.",
    "Kurangi pemakaian air panas dan gunakan mode hemat energi di peralatan rumah tangga.",
    "Cuci pakaian dengan air dingin dan keringkan secara alami untuk mengurangi pemakaian listrik.",
    "Pastikan peralatan rumah tangga dirawat secara berkala agar tetap efisien."
]


recycling_centers = [
    {
        "name": "Pusat Daur Ulang Jambangan",
        "address": "MPM8+2PJ, Jambangan, Kec. Jambangan, Surabaya, Jawa Timur 60232",
        "image_path": "Bot_environment/map_pic/jambangan.png" 
    },
    {
        "name": "Bank Sampah Induk Surabaya",
        "address": "Jl. Raya Menur No.31-A, Manyar Sabrangan, Kec. Mulyorejo, Surabaya, Jawa Timur 60116",
        "image_path": "Bot_environment/map_pic/mulyorejo.png"
    },
    {
        "name": "Komunitas Nol Sampah Surabaya",
        "address": "Jl. Wiguna Timur VI No.10, Gn. Anyar Tambak, Kec. Gn. Anyar, Surabaya, Jawa Timur 60294",
        "image_path": "Bot_environment/map_pic/wiguna.png"
    }

]

zero_waste_challenges = [
    "Selama seminggu, jangan gunakan plastik sekali pakai.",
    "Coba buat kompos dari sisa makanan selama 14 hari.",
    "Beli semua bahan makanan dalam jumlah besar untuk menghindari kemasan.",
    "Coba hidup tanpa sa,mpah selama sehari.",
    "Gantilah produk pembersih dengan yang ramah lingkungan dan tanpa kemasan.",
    "Cobalah membuat sendiri produk perawatan tubuh tanpa kemasan.",
    "Hentikan penggunaan tisu sekali pakai selama seminggu.",
    "Buatlah daftar belanja untuk menghindari pembelian impulsif.",
    "Cobalah untuk membeli hanya barang bekas selama sebulan.",
    "Selama sebulan, catat semua limbah yang Anda hasilkan dan cari cara untuk menguranginya.",
    "Jadikan hari tanpa kendaraan bermotor untuk mengurangi emisi.",
    "Buat kotak penyimpanan untuk barang-barang bekas yang masih bisa digunakan.",
    "Ajak teman untuk melakukan pembersihan pantai atau area publik.",
    "Coba masak semua makanan dari bahan mentah selama seminggu.",
    "Kurangi kebiasaan membeli makanan cepat saji yang dikemas dalam plastik.",
    "Selama sebulan, fokus pada penggunaan produk tanpa kemasan."
]

@bot.command(name='tip')
async def tip(ctx):
    tip = random.choice(waste_reduction_tips)
    await ctx.send(f"Tip untuk mengurangi limbah: {tip}")

@bot.command(name='energy')
async def energy(ctx):
    tip = random.choice(energy_saving_tips)
    await ctx.send(f"Tip hemat energi: {tip}")

@bot.command(name='recycling')
async def recycling(ctx):
    center = recycling_centers[0]
    if os.path.isfile(center['image_path']):
        with open(center['image_path'], 'rb') as f:
            picture = discord.File(f)
        message = f"{center['name']}\nAlamat: {center['address']}"
        await ctx.send(message)
        await ctx.send(file=picture)
    else:
        await ctx.send("Gambar untuk pusat daur ulang tidak ditemukan.")

@bot.command(name='zerowaste')
async def zerowaste(ctx):
    challenge = random.choice(zero_waste_challenges)
    await ctx.send(f"Tantangan Zero-Waste: {challenge}")

@bot.event
async def on_ready():
    print(f"Bot {bot.user} siap membantu!")

bot.run('YourBotToken')
