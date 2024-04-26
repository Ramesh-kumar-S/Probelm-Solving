# text = "loonbalxballpoon"
# text = "balllllllllllloooooooooon"
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
Count = {"b":text.count("b"),
         "a":text.count("a"),
         "l":text.count("l"),
         "o":text.count("o"),
         "n":text.count("n")}
print(Count)
if Count["l"]%2 == 0 and Count["o"]%2 == 0:
    if Count["a"] == Count["b"]:
        print(Count["b"])
    print(0)
    
# if (Count["l"]+Count["o"])%4 == 0 and (Count["b"]+Count["a"]+Count["n"])%3 == 0:
#     print(Count["b"])
# else:
#     print(0)
# print(sum(Count.values())//7)

# l and o  length should be equal
# b,a,n should be less than l and o and b,a,n << l & o //2