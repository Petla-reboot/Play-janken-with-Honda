import time

from pyfiglet import Figlet
if __name__ == '__main__':
    f = Figlet(font='small')
    msg = f.renderText('YOU LOSE')
print("2020年もっと美味しくなったペプシジャパンコーラ飲んでみたくないですか？")
time.sleep(1)
print("僕にじゃんけんで勝ったら")
time.sleep(1)
print("一本あげますよ。")
time.sleep(1)
print("じゃーんけんぽん")
time.sleep(2)
print("あなたは何を出す？")
time.sleep(1)
print("グー＝１、チョキ＝２、パー＝３、ちょっと待って＝４")
a = input(">>")
if a == "4":
	time.sleep(1)
	print("ほな待ちます")
	time.sleep(3)
	print("準備出来ましたか？")
	time.sleep(1)
	print("じゃーんけんぽん")
	time.sleep(2)
	print("あなたは何を出す？")
	time.sleep(1)
	print("グー＝１、チョキ＝２、パー＝３")
	a = input(">>")
	time.sleep(1)
	print(msg)
	time.sleep(1)
	print("俺の勝ち！")
	time.sleep(1)
	print("何事も準備がすべて")
	time.sleep(1)
	print("それを怠っていることがバレてますよ")
	time.sleep(1)
	print("ほな注ぎます")
	time.sleep(1)
	print("めっちゃ美味い！")
	time.sleep(1)
	print("飲みたい？")
	time.sleep(1)
	print("ほな")
	time.sleep(1)
	print("明日も挑戦")
elif a < "4":
	time.sleep(1)
	print(msg)
	time.sleep(1)
	print("俺の勝ち!")
	time.sleep(1)
	print("それで勝てると思ってるんやったら")
	time.sleep(1)
	print("俺がずっと勝ちますよ！")
	time.sleep(1)
	print("ほな注ぎます")
	time.sleep(1)
	print("めっちゃ美味い！")
	time.sleep(1)
	print("飲みたい？")
	time.sleep(1)
	print("ほな")
	time.sleep(1)
	print("明日も挑戦")
	time.sleep(5)
else :
	time.sleep(1)
	print(msg)
	time.sleep(1)
	print("俺の勝ち!")
	time.sleep(1)
	print("お前1～4以外の半角数字以外の文字を入力しただろ")
	time.sleep(1)
	print("それで勝てると思ってるんやったら")
	time.sleep(1)
	print("俺がずっと勝ちますよ！")
	time.sleep(1)
	print("ほな注ぎます")
	time.sleep(1)
	print("めっちゃ美味い！")
	time.sleep(1)
	print("飲みたい？")
	time.sleep(1)
	for counter in range(15):
		print(msg)
		print("言うこと聞かない奴にはあげねえよｗｗｗ")
		time.sleep(1)
