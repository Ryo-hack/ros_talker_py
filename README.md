# ros_talker_py

## セットアップ
### Open JTalkのセットアップ
`apt-get`にて open-jtalk (1.07)をインストールします。

```bash:Terminal
$ sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001
```

`mecab`の辞書は、`/var/lib/mecab/dic/open-jtalk/naist-jdic/` にインストールされます。

### 音声ファイルのセットアップ

MMDAgentから、Voiceデータを流用します。`MMDAgent_Example-1.6.zip` は11MBあります。

```bash:Terminal
$ wget https://sourceforge.net/projects/mmdagent/files/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip/download -O MMDAgent_Example-1.6.zip
```

つぎに`.htsvoice`ファイルを抽出

```bash:Terminal
$ unzip MMDAgent_Example-1.6.zip MMDAgent_Example-1.6/Voice/*
```

ファイルを hts-voice-nitechと同じ場所にコピーしておきます

```bash:Terminal
$ sudo cp -r MMDAgent_Example-1.6/Voice/mei/ /usr/share/hts-voice
```
