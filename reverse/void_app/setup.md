## Setup

Build app with Android Studio:

Choose New Project -> Select Basic Activity -> use Java or Open a project

After coding: File -> Build apk  

Remove debug mode in `./VoidApp/app/build.gradle.kts` : https://developer.android.com/studio/publish/preparing#kts

Build with Generated Signed Bundle/Apk -> create Keystore -> Select release 

Find the app in `./VoidApp/app/release/app-release.apk`
