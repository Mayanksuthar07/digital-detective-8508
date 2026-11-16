# Project ko samjho

Yeh ek computer-basics assignment hai. Isme ek badi app banane ki jagah har topic ka chhota practical aur uski explanation hai.

## Har mission mein kya hai

| Mission | Simple meaning | Kya dekhna hai |
| --- | --- | --- |
| 0 | Project ka setup | Folder structure aur Python/Git versions |
| 1 | Computer input ka result kaise banata hai | IPOS aur hardware/software tables |
| 2 | Terminal se files manage karna | Original file, backup, commands aur output |
| 3 | OS computer ko kaise manage karta hai | Running processes, storage, paths aur permissions |
| 4 | Program run karna | `hello.py` aur compiler/interpreter comparison |
| 5 | Ek number ko alag bases mein likhna | Conversion steps aur Python converter |
| 6 | Changes ka record aur review | Git commits, `update-about` branch aur PR #1 |
| 7 | Website tak request kaise pahunchti hai | DNS, router, server aur actual network checks |
| 8 | Sab files ka final review | Checklist, verification aur submission status |

## Number converter ka logic

```python
number = int(input("Enter a non-negative decimal integer: "))
```

`input()` keyboard se text leta hai. Agar 13 type karo, pehle woh string `"13"` hoti hai. `int()` usko integer 13 banata hai.

```python
print("Binary:", bin(number))
print("Hexadecimal:", hex(number))
```

`bin(13)` ka answer `0b1101` hai. `hex(13)` ka answer `0xd` hai. `0b` binary aur `0x` hexadecimal ka prefix hai. Number ki value dono jagah 13 hi hai.

`try/except ValueError` galat input, jaise `abc` ya `3.5`, par simple message deta hai. `number < 0` negative value check karta hai. `EOFError` ka matlab input stream band ho gayi. `main()` in steps ko ek function mein rakhta hai; last wala `if __name__ == "__main__"` script directly run hone par main ko call karta hai.

## 13 binary mein 1101 kyon hai?

Binary ke place values right se 1, 2, 4, 8 hote hain.

```text
Digits:        1  1  0  1
Place values:  8  4  2  1
Total:         8 + 4 + 0 + 1 = 13
```

Hexadecimal base 16 hai. Usme A=10, B=11, C=12, D=13, E=14 aur F=15 hote hain.

## Terminal ke important differences

- `pwd`: abhi kis folder mein ho.
- `ls`: us folder mein kya hai.
- `cd`: doosre folder mein jaana.
- `cp`: file ki copy banana; original bacha rahta hai.
- `mv`: file ko rename ya move karna.
- `>`: file ka purana content replace karna.
- `>>`: purana content bachakar end mein add karna.
- `|`: left command ka output right command ko dena.

Practice file ko dobara chalane se pehle uska content dekh lena; `>` use karne par purana text replace hoga.

## Git ka flow

```text
File edit -> git add -> git commit -> git push
```

`add` next commit ke liye changes select karta hai. `commit` local history mein version save karta hai. `push` woh commits GitHub par bhejta hai.

Branch ek alag development line hai. Pull Request us branch ke change ko main mein laane ka review proposal hai. [PR #1](https://github.com/Mayanksuthar07/digital-detective-8508/pull/1) open hai: usme root README ki My Learning section hai. Instructor ke kehne tak merge nahi kiya gaya.

## Networking ka flow

Browser client hai. DNS website ka address dhoondhne mein help karta hai. Router data ko networks ke beech forward karta hai. Server request ka response deta hai aur browser page dikhata hai.

`ping` reply aur delay check karta hai. `nslookup` DNS answer dikhata hai. `curl -I` website ke response headers check karta hai. Is run mein 3/3 ping replies aur HTTP 200 mila; har network par numbers same hona zaroori nahi hai.

## Apni understanding check karo

1. 25 ko binary mein convert karke bina code dekhe explain karo.
2. Converter mein 31, 0 aur `hello` daal kar outputs compare karo.
3. `git status` aur `git log --oneline -5` ka difference batao.
4. RAM aur SSD mein kya difference hai?
5. File par `rw-` permission ka kya matlab hai?
6. DNS lookup successful ho lekin website na khule, kya yeh possible hai? Haan: DNS ke baad connection, TLS ya server mein problem ho sakti hai.

Submission se pehle README explanations padho aur jahan zaroori ho apne words mein edit karo. Personal learning aur observations ko khud verify karna baaki hai. Instructor ka form submit nahi hua hai.
