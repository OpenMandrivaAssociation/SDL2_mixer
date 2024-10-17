%define major 0
%define api 2.0
%define libname %mklibname %{name}
%define oldlibname %mklibname %{name} 2.0 0
%define devname %mklibname %{name} -d
%define _disable_lto 1

Summary:	Simple DirectMedia Layer 2 - mixer
Name:		SDL2_mixer
Version:	2.8.0
Release:	1
License:	Zlib
Group:		System/Libraries
Url:		https://www.libsdl.org/projects/SDL_mixer/
Source0:	https://github.com/libsdl-org/SDL_mixer/releases/download/release-%{version}/SDL2_mixer-%{version}.tar.gz
BuildRequires:	libmikmod-devel
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)

%description
SDL2_mixer is a sample multi-channel audio mixer library. It supports any
number of simultaneously playing channels of 16 bit stereo audio, plus a
single channel of music, mixed by the popular MikMod MOD, Timidity MIDI
and SMPEG MP3 libraries.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
%doc README.txt CHANGES.txt
%{_libdir}/lib%{name}.so
%{_includedir}/SDL2/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/SDL2_mixer/
#----------------------------------------------------------------------------

%package -n %{name}-player
Summary:	Players using %{name}
Group:		System/Libraries
Conflicts:	SDL_mixer-player

%description -n %{name}-player
This package contains binary to test the associated library.

%files -n %{name}-player
%doc README.txt
%{_bindir}/playwave
%{_bindir}/playmus

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-music-mod \
	--disable-music-ogg-shared \
	--disable-music-flac-shared
%make_build

%install
%make_install install-bin

