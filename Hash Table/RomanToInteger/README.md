## 13. Roman to Integer (https://leetcode.com/problems/roman-to-integer/) ##

- 설명: input으로 로마 숫자가 주어지면 이를 대응되는 정수로 변환하는 문제

![image](https://user-images.githubusercontent.com/79184083/223020885-2f11b890-b3ea-4997-bfdf-090f19bc048d.png)

- 주의할 점: 

  1. 숫자 4의 경우 로마 숫자 1(I)을 4번 이어 붙이는 방식이 아니라 로마 숫자 5(V)의 앞에 붙여 표기: IV
  2. 9 역시 마찬가지로 로마 숫자 1(I)를 로마 숫자 10(X)의 앞에 붙여 표기: IX
  3. 이러한 규칙이 40(XL), 90(XC), 400(CD), 900(CM)에도 적용됨
  
- 힌트: Problem is simpler to solve by working the string from back to front and using a map.

  1. input으로 주어지는 로마 숫자는 '주의할 점'을 제외하고는 뒤로 갈수록 더 작음
  2. 주어진 문자열을 뒤에서부터 읽어 대응되는 숫자를 더해주되, 만약 연이어 나온 문자열이 더 작은 정수에 대응된다면 빼줌
  3. map을 사용하라는 의미는 dictionary를 생각!
