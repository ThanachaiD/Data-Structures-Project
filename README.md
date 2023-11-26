# Data-Structures-Project

## แนวคิดหลักของโปรแกรม

Graphical User Interface (GUI) ด้วย Tkinter:

Tkinter ถูกใช้เพื่อสร้างและจัดการหน้าต่างแอปพลิเคชัน ปุ่ม (buttons) ช่องข้อความ (entry widgets) และอื่นๆ
การจัดวาง widget ใน Tkinter ทำผ่าน pack() ซึ่งเป็นวิธีง่ายๆ ในการจัดวางองค์ประกอบต่างๆ ในหน้าต่าง

การจัดการข้อมูลพจนานุกรม:

ข้อมูลของพจนานุกรมถูกจัดเก็บในรูปแบบของ dictionary ใน Python ซึ่งเป็นโครงสร้างข้อมูลที่เหมาะสมสำหรับการเก็บคู่คำศัพท์และคำแปล
การเพิ่ม ลบ และอัปเดตข้อมูลในพจนานุกรมสามารถทำได้ง่ายดายผ่านการจัดการกับ dictionary

การบันทึกและโหลดข้อมูลใช้ JSON:

JSON (JavaScript Object Notation) ถูกใช้เพื่อจัดเก็บข้อมูลพจนานุกรมเป็นไฟล์
JSON เป็นรูปแบบที่เหมาะสมสำหรับการจัดเก็บข้อมูลเชิงโครงสร้างเพราะมันสามารถถูกอ่านและเขียนได้ง่าย

## โครงสร้างข้อมูลและการเลือกใช้งาน

Dictionary ใน Python:

การใช้ dictionary ใน Python เป็นตัวเลือกที่เหมาะสมสำหรับการจัดเก็บคู่คำศัพท์และคำแปล ช่วยให้สามารถค้นหา เพิ่ม และลบข้อมูลได้อย่างรวดเร็ว
Dictionary ใช้(key) เพื่อเก็บคำศัพท์ ซึ่งในกรณีนี้คือคำศัพท์ภาษาอังกฤษ และค่าที่เกี่ยวข้องเป็นคำแปลภาษาไทยและชนิดของคำ

Listbox สำหรับแสดงรายการคำศัพท์:

Listbox ใน Tkinter ถูกใช้เพื่อแสดงรายการคำศัพท์ทั้งหมด มันเป็นวิธีที่ดีในการแสดงรายการที่ผู้ใช้สามารถเลือกได้
การใช้ Listbox ทำให้ผู้ใช้สามารถเลือกและดูรายละเอียดของแต่ละคำศัพท์ได้

โปรแกรมนี้ใช้ Python และ Tkinter เพื่อสร้างแอปพลิเคชันแบบเดสก์ท็อปที่มีการโต้ตอบกับผู้ใช้ และการใช้ JSON เพื่อจัดเก็บและจัดการข้อมูลเชิงโครงสร้าง

## รูปผลลัพธ์

การ Search หาคำศัพท์

<img width="406" alt="1" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/c87a293c-7eb7-4775-8030-4c6cc7b7b655">  <img width="404" alt="2" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/52880ddf-ff0a-4004-a939-be66f4adc001">

การเพิ่มคำศัพท์

<img width="411" alt="3" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/f4819b4a-8bdd-4d7e-8262-5082431e225c">  <img width="409" alt="4" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/d2b27e99-4873-4f92-b4ac-3faad63c869c">
<img width="410" alt="5" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/4cfd4ca6-7344-46c4-ba70-22d5b019b9db">  <img width="412" alt="6" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/3ea15b21-9312-4e6b-a353-481f6ca0ca46">

การลบคำศัพท์

<img width="409" alt="7" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/463feb23-15fe-42f9-8e12-343eb1d0d9d7">  <img width="409" alt="8" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/fd0495c4-183b-4cf4-aec8-44d007bf5623">

การแก้ไขคำแปลและชนิดของคำ

<img width="409" alt="9" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/6c1b612a-5a14-487e-aef8-61a585c38077">  <img width="406" alt="10" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/71b7f16f-7c1e-4091-901d-5d207559dd5f">
<img width="406" alt="11" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/cada3737-1515-4ad8-be35-11efaedafb95">  <img width="407" alt="12" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/6fd84156-4d58-464c-a823-430500173b6f">
<img width="409" alt="13" src="https://github.com/ThanachaiD/Data-Structures-Project/assets/148684074/0e5ef44f-cd81-4d36-9984-7d0467c89887">
