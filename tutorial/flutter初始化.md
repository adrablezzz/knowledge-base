# Flutter 项目初始化教程

> 适用版本：Flutter 3.x | Dart 3.x | 更新于 2026-04

---

## 目录

1. [环境准备](#1-环境准备)
2. [安装 Flutter SDK](#2-安装-flutter-sdk)
3. [配置环境变量](#3-配置环境变量)
4. [安装依赖工具](#4-安装依赖工具)
5. [运行 flutter doctor](#5-运行-flutter-doctor)
6. [创建项目](#6-创建项目)
7. [项目结构说明](#7-项目结构说明)
8. [运行项目](#8-运行项目)
9. [常用初始化命令速查](#9-常用初始化命令速查)
10. [常见问题](#10-常见问题)

---

## 1. 环境准备

### 系统要求

| 平台 | 操作系统 | 最低要求 |
|------|----------|----------|
| macOS | macOS 12 Monterey 及以上 | Apple Silicon 或 Intel |
| Windows | Windows 10 64-bit 及以上 | x86-64 |
| Linux | Ubuntu 20.04 / Debian 11 及以上 | x86-64 |

### 前置软件

| 软件 | 用途 | 最低版本 |
|------|------|----------|
| Git | 版本控制 / Flutter 自身依赖 | 2.x |
| Android Studio | Android 开发 + 模拟器 | Hedgehog (2023.1.1) |
| Xcode | iOS / macOS 开发（仅 macOS）| 15.x |
| VS Code（可选）| 推荐编辑器 | 最新版 |

---

## 2. 安装 Flutter SDK

### macOS / Linux

```bash
# 下载 SDK（以 macOS ARM 为例，按实际平台替换）
curl -O https://storage.googleapis.com/flutter_infra_release/releases/stable/macos/flutter_macos_arm64_3.x.x-stable.zip

# 解压到你习惯的目录（推荐 ~/development）
mkdir -p ~/development
unzip flutter_macos_arm64_3.x.x-stable.zip -d ~/development
```

> 💡 也可以通过 [Flutter 官网](https://docs.flutter.dev/get-started/install) 下载对应平台的最新稳定版。

### Windows

```powershell
# 推荐直接从官网下载 .zip 安装包
# 解压到无空格、无中文的路径，例如：
C:\dev\flutter
```

> ⚠️ **不要**将 Flutter 放在 `C:\Program Files\` 或含空格的路径下，会导致构建失败。

### 通过 Git 安装（所有平台可用）

```bash
git clone https://github.com/flutter/flutter.git -b stable ~/development/flutter
```

---

## 3. 配置环境变量

### macOS / Linux（bash 或 zsh）

```bash
# 打开配置文件
# bash 用户：
nano ~/.bashrc

# zsh 用户（macOS 默认）：
nano ~/.zshrc

# 在文件末尾添加以下内容：
export PATH="$HOME/development/flutter/bin:$PATH"

# 保存后让配置生效
source ~/.zshrc    # 或 source ~/.bashrc
```

### Windows（PowerShell）

```powershell
# 将 flutter/bin 添加到系统 PATH
# 方式一：图形界面
# 系统属性 → 高级 → 环境变量 → Path → 新建
# 填入：C:\dev\flutter\bin

# 方式二：PowerShell 命令
$env:Path += ";C:\dev\flutter\bin"
[System.Environment]::SetEnvironmentVariable("Path", $env:Path, "Machine")
```

### 验证配置是否生效

```bash
flutter --version
# 预期输出：
# Flutter 3.x.x • channel stable • ...
# Dart 3.x.x • DevTools 2.x.x
```

---

## 4. 安装依赖工具

### Android 开发环境

```bash
# 1. 安装 Android Studio 后，打开并完成初始设置向导

# 2. 安装 Android SDK Command-line Tools
# Android Studio → SDK Manager → SDK Tools → 勾选 Android SDK Command-line Tools

# 3. 接受 Android 许可证（必须执行）
flutter doctor --android-licenses
# 全部输入 y 同意
```

### iOS 开发环境（仅 macOS）

```bash
# 1. 安装 Xcode（从 App Store）

# 2. 安装 CocoaPods（iOS 依赖管理）
sudo gem install cocoapods

# 或使用 Homebrew：
brew install cocoapods

# 3. 接受 Xcode 许可证
sudo xcodebuild -license accept

# 4. 安装 iOS 模拟器组件
xcodebuild -downloadPlatform iOS
```

### VS Code 插件（推荐）

在 VS Code 扩展市场搜索并安装：

- **Flutter**（by Dart Code）— 必装，包含调试、热重载
- **Dart**（by Dart Code）— 必装，语言支持
- **Pubspec Assist** — 快速添加依赖
- **Flutter Widget Snippets** — 常用 Widget 代码片段

---

## 5. 运行 flutter doctor

```bash
flutter doctor
```

### 理想输出示例

```
Doctor summary (to see all details, run flutter doctor -v):
[✓] Flutter (Channel stable, 3.x.x)
[✓] Android toolchain - develop for Android devices
[✓] Xcode - develop for iOS and macOS
[✓] Chrome - develop for the web
[✓] Android Studio (version 2023.x)
[✓] VS Code (version 1.x)
[✓] Connected device (2 available)
[✓] Network resources

• No issues found!
```

### 常见错误处理

| 错误信息 | 原因 | 解决方案 |
|----------|------|----------|
| `Android toolchain [✗]` | 未接受许可证 | 执行 `flutter doctor --android-licenses` |
| `CocoaPods not installed` | macOS 缺少 CocoaPods | `sudo gem install cocoapods` |
| `Xcode [✗]` | Xcode 未安装或版本过低 | 从 App Store 安装/更新 |
| `cmdline-tools component is missing` | 缺少 Android 命令行工具 | Android Studio SDK Manager 中安装 |

> 💡 运行 `flutter doctor -v` 可获取更详细的诊断信息。

---

## 6. 创建项目

### 基础创建命令

```bash
# 创建新项目（最常用方式）
flutter create my_app

# 进入项目目录
cd my_app
```

### 常用创建参数

```bash
# 指定包名（推荐，发布时必须唯一）
flutter create --org com.yourcompany my_app

# 指定支持的平台（减少不需要的平台代码）
flutter create --platforms android,ios my_app

# 指定项目模板
flutter create --template=app my_app        # 默认完整 App
flutter create --template=package my_pkg    # 纯 Dart 包
flutter create --template=plugin my_plugin  # 平台插件

# 指定 Dart SDK 版本语言特性
flutter create --platform android,ios --org com.example my_app

# 完整示例：带包名 + 指定平台
flutter create \
  --org com.yourcompany \
  --platforms android,ios,web \
  my_app
```

---

## 7. 项目结构说明

```
my_app/
├── android/          # Android 原生代码（一般不需要手动修改）
├── ios/              # iOS 原生代码
├── web/              # Web 平台代码（如启用）
├── lib/              # ★ 主要开发目录
│   └── main.dart     # 应用入口文件
├── test/             # 单元测试 / Widget 测试
├── assets/           # 静态资源（图片、字体等，需在 pubspec.yaml 注册）
├── pubspec.yaml      # ★ 项目配置 + 依赖管理（类似 package.json）
├── pubspec.lock      # 依赖版本锁定（提交到 Git）
└── .gitignore        # 建议将 /build 加入忽略
```

### pubspec.yaml 关键字段说明

```yaml
name: my_app                    # 项目名，用于内部引用
description: A Flutter project  # 描述
version: 1.0.0+1                # 版本号：语义版本+构建号

environment:
  sdk: ">=3.0.0 <4.0.0"        # Dart SDK 版本约束

dependencies:                   # 运行时依赖
  flutter:
    sdk: flutter
  http: ^1.2.0                  # 示例：添加 http 包

dev_dependencies:               # 开发时依赖（不打入生产包）
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

flutter:
  uses-material-design: true
  assets:                       # 注册静态资源
    - assets/images/
  fonts:                        # 注册自定义字体
    - family: MyFont
      fonts:
        - asset: assets/fonts/MyFont-Regular.ttf
```

---

## 8. 运行项目

### 查看可用设备

```bash
flutter devices
# 输出示例：
# iPhone 15 Pro (mobile) • 00001234-... • ios     • iOS 17.x
# Android SDK built for x86 (mobile) • emulator-5554 • android
# Chrome (web) • chrome • web-javascript • Google Chrome 12x
# macOS (desktop) • macos • darwin-arm64 • macOS 14.x
```

### 运行命令

```bash
# 运行（自动选择可用设备）
flutter run

# 指定设备运行
flutter run -d emulator-5554   # Android 模拟器
flutter run -d iphone          # iOS 模拟器（模糊匹配）
flutter run -d chrome          # 浏览器
flutter run -d macos           # macOS 桌面

# 以 release 模式运行（接近生产性能）
flutter run --release
```

### 热重载与热重启

在 `flutter run` 运行中，终端输入：

| 按键 | 功能 | 说明 |
|------|------|------|
| `r` | 热重载（Hot Reload） | 保留状态，刷新 UI，最常用 |
| `R` | 热重启（Hot Restart） | 重置状态，重新执行 main() |
| `q` | 退出 | 停止运行 |
| `p` | 显示 Widget 边界 | 调试布局 |
| `i` | 显示 Inspector | 调试 Widget 树 |

---

## 9. 常用初始化命令速查

```bash
# ── 环境相关 ─────────────────────────────────────────
flutter --version                   # 查看版本
flutter upgrade                     # 升级 Flutter
flutter doctor                      # 环境检查
flutter doctor -v                   # 详细环境检查
flutter doctor --android-licenses   # 接受 Android 许可

# ── 项目创建 ─────────────────────────────────────────
flutter create <name>               # 创建项目
flutter create --org <pkg> <name>   # 指定包名创建
flutter create --template=package   # 创建 Dart 包

# ── 依赖管理 ─────────────────────────────────────────
flutter pub get                     # 安装依赖
flutter pub upgrade                 # 升级所有依赖
flutter pub add http                # 添加单个依赖
flutter pub remove http             # 移除依赖
flutter pub outdated                # 检查过期依赖

# ── 构建 ─────────────────────────────────────────────
flutter build apk                   # 构建 Android APK
flutter build appbundle             # 构建 Android AAB（上架用）
flutter build ios                   # 构建 iOS（需 Mac + Xcode）
flutter build web                   # 构建 Web
flutter build macos                 # 构建 macOS 桌面

# ── 调试与测试 ────────────────────────────────────────
flutter run                         # 运行（debug 模式）
flutter run --release               # 运行（release 模式）
flutter test                        # 运行所有测试
flutter analyze                     # 静态代码分析
flutter clean                       # 清除构建缓存

# ── 设备 ─────────────────────────────────────────────
flutter devices                     # 列出可用设备
flutter emulators                   # 列出可用模拟器
flutter emulators --launch <id>     # 启动指定模拟器
```

---

## 10. 常见问题

### Q: `flutter pub get` 速度很慢或失败

```bash
# 配置国内镜像（中国大陆推荐）
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn

# 建议写入 ~/.zshrc 或 ~/.bashrc 持久化
```

### Q: Android Studio 找不到 SDK

```bash
# 手动指定 Android SDK 路径
flutter config --android-sdk /path/to/android/sdk

# 查看当前配置
flutter config
```

### Q: iOS 构建报 CocoaPods 错误

```bash
cd ios
pod install --repo-update
cd ..
flutter run
```

### Q: `flutter clean` 后运行报错

```bash
flutter clean
flutter pub get
flutter run
```

> 💡 遇到奇怪的构建错误，90% 的情况执行以上三步可以解决。

### Q: 热重载没有生效

热重载不支持以下场景的变更，需要热重启（`R`）：
- 修改 `main()` 函数
- 修改全局变量初始值
- 修改 `initState()` 逻辑
- 添加新的依赖包

---

## 参考资料

- [Flutter 官方文档](https://docs.flutter.dev)
- [pub.dev 包管理](https://pub.dev)
- [Flutter GitHub](https://github.com/flutter/flutter)
- [Flutter 中文网](https://flutter.cn)