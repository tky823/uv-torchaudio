# uv-torchaudio

Repository to use FFmpeg backend by torchaudio using uv.
We mainly focus on MacOS.

## MacOS

```sh
brew install ffmpeg@6  # torchaudio supports versions 4, 5, and 6.
homebrew_prefix="${HOMEBREW_PREFIX}"  # or homebrew_prefix="$(brew --prefix)"
export DYLD_FALLBACK_LIBRARY_PATH="${homebrew_prefix}/opt/ffmpeg@6/lib"
python -c "import torchaudio; print(torchaudio.list_audio_backends())"
```
