# Unity-AssetDuplicator
Problum : 
When you duplicate a folder in Unity, it generates copies of all the files, but the references still remain directed towards the original folder.

Solution : 
Create a copy of a folder containing assets while ensuring that their references are retained within the same folder by updateing GUIDs in meta referece.

Required :
1. python 3.5 or above. 
2. Mac OS.

How to use :
1. Go to Unity asset folder in finder. (Close Unity if it is open)
2. Make a copy of the folder that requires dupication.
3. Move this folder to outside the Unity project folder. (in to the folder this script is added)
4. Remove any scripts.
5. Remove assets & folders that you dont want to dupicat.
6. Copy folder name.
7. Open terminal and naviage to the folder this script is present.
8. Run the script in terminal by "python3 DuplicateFolder.py -i Folder name" (replace Folder name with the name you just copied)
9. Move the folder back Unity project.
10. Open Unity and let it import.


Termincal command : python DuplicateFolder.py -i Folder name

