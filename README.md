# main homepage

このリポジトリには、シンプルなポモロードタイマーのウェブページが含まれています。HTML と JavaScript だけで動作するため、特別な開発環境は不要です。

## 使い方

1. 上の **Code** ボタンから ZIP をダウンロードするか、`git clone` でリポジトリを取得します。
2. フォルダー内の `index.html` をブラウザーで開きます。
   - **Windows**: エクスプローラーで `index.html` をダブルクリックします。
   - **macOS**: Finder で `index.html` をダブルクリックします。
   - **Linux**: ファイルマネージャーから開くか、端末で `xdg-open index.html` を実行します。
3. ブラウザーが起動すると中央に **25:00** と表示されたタイマーが見えます。
   - **Start**: タイマーを開始します。
   - **Stop**: 一時停止します。
   - **Reset**: 25 分から再スタートします。

### 開けない場合

ブラウザーが起動しない場合は、端末で次のコマンドを実行して簡易的な Web サーバーを起動し、`http://localhost:8000/index.html` を開いてください。

```bash
python3 -m http.server
```

## Timer behavior

After each work period ends, an alert notifies you to take a 5-minute break. When the break finishes, another alert tells you to get back to work. The timer automatically alternates between work and break intervals.
