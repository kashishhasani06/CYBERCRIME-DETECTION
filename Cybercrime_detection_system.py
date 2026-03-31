while True:
      print("CYBERCRIME DETECTION TOOL")
      print("select the tool you want to use:")
      print("1. Messages scam detector")
      print("2. Malicious link detector")
      print("3. phone number analyzer")
      print("4. exit")
      choice = input("\nEnter you choice:")

      if choice =="1":
         msg = input("\nEnter message: ").lower().split()

         messages=[
      "win money now",
      "claim your reward",
      "click the link ",
      "let's meet after the class",
      "kyc updated successfully",
      "win lottery claim now",
      "metting at 10am",
      "submission deadline",
      "balance is 10000",
      "send OTP NOW"

         ]
         labels=[1,1,1,0,0,1,0,0,0,1] #1=phishing , #0=safe
         word_scores={}
         word_count={}

         for i in range(len(messages)):
            words= messages[i].lower().split()
            label=labels[i]
            for word in words:
               if word not in word_scores:
                  word_scores[word]=0
                  word_count[word]=0

               word_count[word] += 1

               if label==1:
                  word_scores[word] += 2
               else:
                  word_scores[word] -= 1

            scores=0
            matched_words=[]

         for word in msg:
            if word in word_scores:
                  scores += word_scores[word]
                  matched_words.append(word)
                  
         if len(msg) > 0:
                  final_score= scores/len(msg)
         else:
                  final_score=0

      
         if final_score> 0.5:
                  print("PHISHING MESSAGES")
         else:
                  print("SAFE MESSAGES")
                  print("\nRESULT")
                  print("score:",round(final_score,2))
                  print("Matched words:",matched_words)
            
      elif choice =="2":
         url = input("\nEnter URL: ").lower()
         risk = 0
         reasons = []
         if len(url) > 100:
            risk += 10
            reasons.append("Long URL")
         if url.startswith("http://"):
            risk += 15
            reasons.append("Not secure (HTTP)")
         if "@" in url:
            risk += 25
            reasons.append("@ symbol used")
         if url.count(".") > 3:
            risk += 10
            reasons.append("Too many dots")
         if "-" in url:
            risk += 5
            reasons.append("Hyphen used")
         keywords = ["login", "verify", "update", "bank", "account"]
         for word in keywords:
            if word in url:
                  risk += 10
                  reasons.append("Keyword: " + word)
         if "http" in url:
            risk += 20
         if risk >= 40:
            status = " Dangerous Link"
         elif risk > 25:
            status = " Suspicious Link"
         else:
            status = " Safe Link"

         print("\n--- RESULT ---")
         print("Status:", status)
         print("Risk Score:", risk)
         print("Reasons:", ", ".join(reasons))
      elif choice == "3":
         number = input("\nEnter phone number: ")

         risk = 0
         reasons = []
         operator = "Unknown"
         location = "Unknown"

         if len(number) != 10 or not number.isdigit():
            print(" Invalid number format")
            continue

         prefix = number[:2]
         if prefix in ["98", "99"]:
            operator = "Possible: Airtel/Vodafone"
            location = "North India"
         elif prefix in ["97", "96"]:
            operator = "Possible: Vodafone/Idea"
            location = "West India"
         elif prefix in ["70", "71"]:
            operator = "Possible: Jio"
            location = "All India"
         elif prefix in ["88", "89"]:
            operator = "Possible: BSNL"
            location = "India"

         if number == number[0] * 10:
            risk += 25
            reasons.append("All digits same")

         if "0000" in number or "1234" in number:
            risk += 15
            reasons.append("Suspicious pattern")

         if number[0] not in ["6", "7", "8", "9"]:
            risk += 20
            reasons.append("Invalid start digit")

         if risk >= 40:
            status = " Likely Scam Caller"
         elif risk >= 20:
            status = "Suspicious Number"
         else:
            status = " Likely Safe"

         print("\n--- NUMBER ANALYSIS ---")
         print("Status:", status)
         print("Estimated Operator:", operator)
         print("Region:", location)
         print("Risk Score:", risk)
         print("Reasons:", ", ".join(reasons) if reasons else "No major issues")
         print("\nNote: Operator is estimated based on number series and may vary due to mobile number portability.")
      elif choice == "4":
         print("\nExiting system... Stay safe! ")
         break
      else:
         print("\n Invalid choice. Please select 1-4.")


      


      
