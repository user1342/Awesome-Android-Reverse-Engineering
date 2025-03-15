# Awesome Android Reverse Engineering
<p align="center">
   <img width=100% src="assets/cover.gif">
 </a>
</p>


<p align="center">
 <b>A curated list of awesome Android Reverse Engineering training, resources, and tools.</b>


<div align="center">


[![Awesome](https://awesome.re/badge.svg)](https://github.com/MarketingPipeline/Awesome-Repo-Template/)
![GitHub contributors](https://img.shields.io/github/contributors/user1342/Awesome-Android-Reverse-Engineering)
![GitHub Repo stars](https://img.shields.io/github/stars/user1342/Awesome-Android-Reverse-Engineering?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/user1342/Awesome-Android-Reverse-Engineering?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/user1342/Awesome-Android-Reverse-Engineering)
<br>

</div>

# How to Use
Awesome-Android-Reverse-Engineering is an amazing list for people who work in taking apart Android applications, systems, or components. Simply press ```ctrl + F``` to search for a keyword, go through our Contents Menu, or lookout for a '☆' indicating some great and up-to-date resources.

# Contents
- [Training](#training)
  - [Courses and Material](#courses-and-material)
  - [Videos](#videos)
  - [Books](#books)
- [Tools](#tools)
  - [Static Analysis Tools](#static-analysis-tools)
  - [Dynamic Analysis Tools](#dynamic-analysis-tools)
  - [Decompilers](#decompilers)
  - [Malware Analysis](#malware-analysis)
- [Resources](#resources)
  - [Documentation](#documentation)
  - [Case Studies](#case-studies)
- [CTFs and CrackMes](#ctfs-and-crackmes)
- [Misc](#misc)
- [Obfuscation & Anti-Reversing](#obfuscation--anti-reversing)
- [Firmware & Kernel Analysis](#firmware--kernel-analysis)
- [Cloud API & Web Services Reversing](#cloud-api--web-services-reversing)

## Training

### Courses and Material
- [☆ Maddie Stone's Android Reverse Engineering Training](https://www.ragingrock.com/AndroidAppRE/) - A comprehensive online training course on Android reverse engineering by Maddie Stone.
- [Introduction to Assembly from Azeria Labs](https://azeria-labs.com/writing-arm-assembly-part-1/) - Covering everything from data types, registers, the ARM instruction set, memory instructions, and more.

### Videos
- [Kristina Balaam Android Reverse Engineering](https://www.youtube.com/@chmodxx) - A video series on reverse engineering basics and reverse engineering Android malware.
- [LaurieWired Android Reverse Engineering videos](https://www.youtube.com/@lauriewired) - A YouTube channel focusing on Android reverse engineering.
- [Using Frida To Modify Android Games | Mobile Dynamic Instrumentation](https://www.youtube.com/watch?v=BXtAujoPhQw) - Focusing on reverse engineering Android applications and on using Frida to dynamically modify Android games.

### Books
- [☆ Android Internals: A Confectioner's Cookbook](http://newandroidbook.com/) - An in-depth exploration of the inner-workings of Android.
- [Blue Fox: Arm Assembly Internals and Reverse Engineering](https://www.amazon.co.uk/dp/1119745306) - Provides a solid foundation in ARM assembly internals.
- [Android Software Internals Quick Reference](https://www.amazon.co.uk/Android-Software-Internals-Quick-Reference/dp/1484269136) - Techniques in Java and Android system internals.
- [☆ Mobile Offensive Security Pocket Guide](https://www.amazon.co.uk/Mobile-Offensive-Security-Pocket-Guide/dp/1399921959) - Key information, approaches, and tooling for mobile penetration testers.
- [Android Security Internals](https://nostarch.com/androidsecurity) - Detailed look into Android security architecture.
- [Android Malware Detection with Machine Learning](https://nostarch.com/androidmalwaredetection) - Machine learning techniques for detecting malicious apps.
- [Android Hacker's Handbook](https://www.amazon.com/Android-Hackers-Handbook-Joshua-Drake/dp/111860864X/) - A deep dive into Android exploitation and forensics.
- [Practical Reverse Engineering](https://www.amazon.com/Practical-Reverse-Engineering-Reversing-Obfuscation/dp/1118787315/) - Covers low-level reverse engineering concepts, including ARM assembly.
- [The IDA Pro Book](https://nostarch.com/idapro2.htm) - Essential for advanced IDA Pro techniques.

## Tools

### Static Analysis Tools
- [QARK](https://github.com/linkedin/qark) - An open-source tool for automatic Android app vulnerability scanning.
- [Quark Engine](https://github.com/quark-engine/quark-engine) - Integrates various tools as Quark Script APIs for mobile security research.
- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) - Supports both static and dynamic analysis for Android app security testing.
- [AndroBugs Framework](https://github.com/AndroBugs/AndroBugs_Framework) - Analyzes and scans Android apps for security issues.
- [☆ imjtool](http://newandroidbook.com/tools/imjtool.html) - Firmware unpacking tool for various vendors and formats.
- [Android Studio](https://developer.android.com/studio) - Useful for analyzing decompiled apps via an IDE.
- [☆ APK Dependency Graph](https://github.com/alexzaitsev/apk-dependency-graph) - Visualizes APK class dependencies.
- [disarm](http://newandroidbook.com/tools/disarm.html) - Command line utility for parsing ARM-64 instructions.
- [COVA](https://github.com/secure-software-engineering/COVA) - Computes path constraints based on user-defined APIs.
- [DIS{integrity}](https://github.com/user1342/DISintegrity) - Analyzes APKs for root, integrity, and tamper detection.
- [Dexcalibur](https://github.com/FrenchYeti/dexcalibur) - Automated tool for analyzing and instrumenting Android applications.

#### De-Obfuscation
- [☆ Obfu[DE]scate](https://github.com/user1342/Obfu-DE-Scate) - De-obfuscation tool that uses fuzzy comparison logic.
- [TinySmaliEmulator](https://github.com/amoulu/TinySmaliEmulator) - Minimalist smali emulator for "decrypting" obfuscated strings.
- [simplify](https://github.com/CalebFenton/simplify) - Android virtual machine and deobfuscator.
- [deoptfuscator](https://github.com/Gyoonus/deoptfuscator) - Tool for deobfuscating apps using control-flow obfuscation.

### Dynamic Analysis Tools
- [Drozer](https://github.com/WithSecureLabs/drozer) - Framework for Android security testing with dynamic analysis features.
- [jtrace](http://newandroidbook.com/tools/jtrace.html) - Similar to strace, but for Android system calls.
- [sesearch](https://linux.die.net/man/1/sesearch) - Command line tool for querying SELinux policies.
- [AutoDroid](https://github.com/user1342/AutoDroid) - Mass APK gathering and analysis tool.
- **Networking:**
  - [☆ Burp Suite](https://portswigger.net/burp) - Commercial tool for analyzing network traffic of Android apps.
  - [Wireshark](https://www.wireshark.org/) - Open-source network protocol analyzer.
  - [SSLsplit](https://github.com/droe/sslsplit) - Intercepts and manipulates SSL/TLS encrypted traffic.
  - [MITMProxy](https://mitmproxy.org/) - Man-in-the-middle proxy for analyzing network traffic.
  - [apk-mitm](https://github.com/shroudedcode/apk-mitm) - Prepares APKs for HTTPS inspection.
- **Dynamic Instrumentation:**
  - [☆ Frida](https://frida.re/) - Dynamic instrumentation toolkit for runtime manipulation.
  - **Xposed Framework** - For hooking and modifying app behavior at runtime.
  - [☆ Objection](https://github.com/sensepost/objection) - Runtime exploration tool to bypass app security controls.
  - [RMS Runtime Mobile Security](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) - Frida web interface.
  - [☆ FriDump](https://github.com/Nightbringer21/fridump) - Uses Frida to dump memory of running apps.
  - [jnitrace](https://github.com/chame1eon/jnitrace) - Frida-based JNI API tracer.
  - [☆ Binder Trace](https://github.com/foundryzero/binder-trace) - Intercepts and parses Android Binder messages.

### Decompilers
- [☆ JADX](https://github.com/skylot/jadx) - Decompiles APKs into Java source code.
- [Procyon](https://github.com/mstrobel/procyon) - Suite of Java decompilation tools.
- [Cfr](https://github.com/leibnitz27/cfr) - Supports decompilation of Android APK files.
- [FernFlower](https://github.com/JetBrains/intellij-community/tree/master/plugins/java-decompiler/engine) - Analytical decompiler for Java.
- [☆ Apktool](https://ibotpeaches.github.io/Apktool/) - Popular tool for decompiling/recompiling APK files.
- [DEX2JAR](https://github.com/pxb1988/dex2jar) - Converts DEX files to JAR files.
- [JDGui](http://java-decompiler.github.io/) - Graphical utility to view Java source from class files.
- [IDA Pro](https://hex-rays.com/ida-pro/) - Commercial disassembler and debugger.
- [☆ Ghidra](https://ghidra-sre.org/) - Free and open-source SRE framework.
- **Additional Decompilers:**
  - JEB Decompiler - Commercial decompiler for Android apps.
  - [Radare2](https://rada.re/n/) - Reverse engineering framework with disassembly and debugging.
  - [Androguard](https://github.com/androguard/androguard) - Analyzes and reverse engineers Android apps.
  - [apk2gold](https://github.com/lxdvs/apk2gold) - Decompiles Android apps to Java (note: may be outdated).
  - [AndroidProjectCreator](https://github.com/ThisIsLibra/AndroidProjectCreator) - Converts APKs to Android Studio projects.
  - [APK Studio](https://github.com/vaibhavpandeyvpz/apkstudio) - Qt-based IDE for reverse-engineering APKs.
  - [show-java](https://github.com/niranjan94/show-java) - APK, JAR & Dex decompiler.
  - [☆ APKLab](https://marketplace.visualstudio.com/items?itemName=Surendrajat.apklab) - VS Code extension integrating multiple tools.

### Malware Analysis 
- [DroidDetective](https://github.com/user1342/DroidDetective) - Machine learning malware analysis for Android apps.
- [Cuckoo Droid](https://github.com/idanr1986/cuckoodroid-2.0) - Automated Android malware analysis with Cuckoo Sandbox.
- [androwarn](https://github.com/maaaaz/androwarn) - Static code analyzer for malicious Android applications.

## Resources

### Documentation
- [Android Security Documentation](https://source.android.com/docs/security) - Official Google documentation on Android security.
- [Android Reverse Engineering Challenges](https://github.com/apsdehal/awesome-ctf#reverse-engineering) - Curated list of reverse engineering challenges and CTFs.
- [AndroidXref](http://androidxref.com/) - Open code search for Android source.
- [APKMirror](https://www.apkmirror.com/) - Repository of APKs from the Play Store and user uploads.
- [APKPure](https://m.apkpure.com/) - Repository of APKs for testing and research.

### Case Studies
- [A Reverse Engineer’s Post-mortem Of The Houseparty Video Chat App](https://www.jamesstevenson.me/a-reverse-engineers-post-mortem-of-the-houseparty-video-chat-app/)
- [SharkBot: a “new” generation Android banking Trojan being distributed on Google Play Store](https://research.nccgroup.com/2022/03/03/sharkbot-a-new-generation-android-banking-trojan-being-distributed-on-google-play-store/)
- [In-the-Wild Series: Android Exploits](https://googleprojectzero.blogspot.com/2021/01/in-wild-series-android-exploits.html)

## CTFs and CrackMes
- [☆ UnCrackable Mobile Apps](https://github.com/OWASP/owasp-mastg/tree/master/Crackmes) - OWASP Android app CrackMes.
- [CyberTruckChallenge19](https://github.com/nowsecure/cybertruckchallenge19) - Security workshop material from CyberTruck Challenge 2019.
- [KGB Messenger](https://github.com/tlamb96/kgb_messenger) - CTF challenge for learning Android reverse engineering.
- [Flare-On Challenge](https://www.fireeye.com/services/flare-on.html) - High-level reverse engineering CTF with Android challenges.
- [OverTheWire Narnia](http://overthewire.org/wargames/narnia/) - Not Android-specific but excellent for binary exploitation practice.

## Misc
- [LADB](https://github.com/tytydraco/LADB) - Local ADB shell for Android.
- [Broken Droid Factory](https://github.com/user1342/Broken-Droid-Factory) - Generates pseudo-random vulnerable Android apps for training.
- [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer) - CLI tool for signing and zip aligning APKs.
- [RUNIC tamper detection demo](https://github.com/user1342/RUNIC) - Demo for understanding Android tamper detection and integrity systems.

## Obfuscation & Anti-Reversing
- **Obfuscation Tools:**
  - [ProGuard](https://www.guardsquare.com/manual/configuration/usage) - Code shrinker, optimizer, and obfuscator.
  - [R8](https://developer.android.com/studio/build/shrink-code) - Google’s code shrinker and obfuscator.
  - [DexGuard](https://www.guardsquare.com/dexguard) - Commercial tool for advanced app obfuscation.
- **Anti-Reversing Techniques:**
  - [Android Tamper Detection Framework (ATDF)](https://github.com/Fuzion24/AndroidTamperDetection) - Implements tamper detection.
  - [Paranoid](https://github.com/sundaysec/Paranoid) - Detects root and tampering.
  - [libhooker](https://github.com/hluwa/libhooker) - Detects hooking frameworks like Frida and Xposed.

## Firmware & Kernel Analysis
- [Binwalk](https://github.com/ReFirmLabs/binwalk) - Analyze, extract, and reverse engineer firmware images.
- [AFLSmart](https://github.com/aflsmart/aflsmart) - Fuzzer optimized for firmware image analysis.
- [Android Kernel Exploits](https://github.com/saelo/android_kernel_exploitation) - Collection of kernel vulnerabilities and exploit techniques.
- [FirmWire](https://github.com/FirmWire/FirmWire) - Dynamic analysis platform for baseband firmware.

## Cloud API & Web Services Reversing
- [Postman](https://www.postman.com/) - API development and testing tool for analyzing Android network interactions.
- [Burp Suite Extensions for Mobile](https://portswigger.net/burp/extensions) - Plugins useful for API reversing.
- [GraphQL Raider](https://github.com/BlackFan/graphql-raider) - Burp Suite extension for discovering and exploiting GraphQL APIs.
- [Mobile API Recon](https://github.com/0xInfection/Mobile-API-Recon) - Automates API discovery in Android apps.

## Contributing
Your contributions are always welcome! Please read the contribution guidelines first. We follow the Contributor Covenant Code of Conduct, so please review and adhere to it when contributing.

## Licence
![GitHub](https://img.shields.io/github/license/user1342/Awesome-Android-Reverse-Engineering)  
This project is licensed under the MIT License - see the LICENSE.md file for details.
