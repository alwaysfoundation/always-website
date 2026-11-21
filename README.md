# alwaysfoundation.org

The Always Foundation website: who we are, docs, stories, partnering with Always, and ideas and problems.

## Build

```sh
cd src && python3 build_site.py   # writes ../index.html
```

The site is one self-contained page with hash routes (`#/docs/…`, `#/join/church`, `#/feedback`). Forms post to the Always API when `API_BASE` is set in `build_site.py`.

## Licences

Code is Apache 2.0 (`LICENSE`). Words and docs are CC BY 4.0 (`CONTENT-LICENSE.md`). The Always name and mark are trademarks (`TRADEMARKS.md`).
