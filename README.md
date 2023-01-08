# domain-word

Tells you which "words" can be written as a publicly available domain.

Domain names that end up being a word after removing the dots are cool.
I guess we all remember [Del.icio.us](https://en.wikipedia.org/wiki/Delicious_(website)),
and some may know [bullsh.it](http://bullsh.it/).

But English has many words, and so do all the other languages.
And there are many TLDs and public suffixes available.
This means many domain "words" aren't taken (or even hogged) yet,
and also that it's not easy to check whether a specific word is taken
(because there could be many suffixes).

This project allows you to quckly (and dirtily) check whether (and how)
a specific word can still be acquired.  There is a surprising number still available:
[ev.il](http://ev.il/), [mourni.ng](http://mourni.ng/), [sna.ps](http://sna.ps), [enor.mo.us](http://enor.mo.us/), etc.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Performance](#performance)
- [Copyright / License](#copyright-license)
- [Contribute](#contribute)

## Install

No need to install it.  There are no dependencies.

## Usage

### For American English

For convenience, the result for a very exhaustive American English wordlist is already available in [`results.txt`](/results.txt).

The output format is quite easy:
```
bathhouses: ['ses', 'es']
```
This means that `ses` is a public suffix and/or a TLD, and so is `es`.

### For your own wordlist

If you want to substitude your own wordlist,
you can replace `src/american-english`.
Or make the code point to your own file.

### As a library

You can even use it as a library!
The easiest way is probably to call `compute_results(wordlist_filename, source_dir=None)` and process the results to your own liking.

## Performance

The American English wordlist seems to be a good benchmark:

The code reads two domain lists with a combined length of over 14,000 lines,
reads the wordlist of over 100,000 words, and outputs all possible combinations
in under 3 seconds (2.7 seconds on my machine).

I'm sure this can be done faster, but I don't see any point in speeding this up.

## Some interesting domains

- [sou.ls](http://sou.ls)
- [skywrite.rs](http://skywrite.rs)
- [gelat.in](http://gelat.in)
- [some.day](http://some.day)
- [s.et](http://s.et)
- [swa.mp](http://swa.mp)
- [bi.ke](http://bi.ke)
- [benefici.al](http://benefici.al)
- [coll.ar](http://coll.ar)

## Copyright / License

I license this project and my code under the MIT License.
So do whatever you want with it.

Copyright and license information for the third-party sources
can be found in `COPYRIGHT.txt`.

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/subint/issues/new) or submit PRs.
