import asyncio
import sys
import crawl

async def main():
    #print("Hello from webcrawler!")

    if len(sys.argv) < 4:
        print("missing arguments - use url, max concurrency, max pages")
        sys.exit(1)
    elif len(sys.argv) > 4:
        print("too many arguments provided")
        sys.exit(1)
    elif sys.argv[2].isdigit() == False or sys.argv[3].isdigit() == False:
        print("max concurrency and max pages must be an integer")
        sys.exit(1)
    elif int(sys.argv[2])<1 or int(sys.argv[3])<1:
        print("max concurrency and max pages must be a positive integer")
        sys.exit(1)
    else:
        print(f"starting crawl of: {sys.argv[1]}")

        try:
            page_data = await crawl.crawl_site_async(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

        except Exception as e:
            print(f"error retreiving HTML from {sys.argv[1]}: {e}")
            sys.exit(1)

        print(f"crawled {len(page_data)} pages:")

        for page in page_data.values():
            print(f"  - {page['url']}: {len(page['outgoing_links'])} outgoing links")

        print("crawl complete")
        
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())
