import sys
import crawl

def main():
    #print("Hello from webcrawler!")

    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)
    else:
        print(f"starting crawl of: {sys.argv[1]}")

        try:
            crawl.crawl_page(sys.argv[1])

        except Exception as e:
            print(f"error retreiving HTML from {sys.argv[1]}: {e}")
            sys.exit(1)

        print("crawl complete")
        
        sys.exit(0)



if __name__ == "__main__":
    main()
