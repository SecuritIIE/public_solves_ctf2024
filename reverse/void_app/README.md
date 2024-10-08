## Solution

It is a basic apk. 
We can use JADX to open it.

In the `AndroiManifest.xml`, there is a MainActivity class identified by the intent `LAUNCHER`.
In this class, there is the Bundle constructor in onCreate(), the menu in onCreateOptionsMenu() with onOptionsItemSelected() settings and the navigation controller in onSupportNavigateUp().
Here are 2 Fragment components displaying a string "Hello player [...] the flag is not here", identified by `R.id.nav_host_fragment_content_main` that we see if we launch the app in Android Studio AVD or with another emulator.

They are loaded with R-Strings which are pointers to existing strings in XML config files.

We can search for strings and find the flag splitted in 7 strings among fragment components strings in `./VoidApp/app/res/values/strings.xml`.
The flag is FSIIECTF{6fd1520dfa5e7de7588289cfbae85f83}.
