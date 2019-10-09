Title: Experimenting with Vim emulations in all apps
Date: 2019-09-18 12:30
Category: vanity, vim

# Background

I spent more or less the first ten years of my career using Linux machines, and the next 11 years using Windows for my day-to-day work.  I used a Mac laptop for most of that time as my personal device, and I'd occasionally do small personal projects with it, but I never really used it for serious development.

I'm back to using Linux now, but the twist is that I access everything from applications running on a Mac laptop.  I've been going slightly crazy because the key bindings in the applications I use (primarily VS Code for development, iTerm2 as a terminal, and Emacs as my research notebook) all support slightly different navigation keys out of the box.  In particular, I found myself getting messed up on shortcuts that use the "meta" key.

# Keymap craziness

In Windows and Linux, the "Alt" key (on either side of the spacebar) is a great "meta" key.  Most system keystrokes use "Control" as the modifier, so "Alt" can mostly be interpreted freely as an Emacs-style modifier.  That's something I've especially relied on for navigation (moving forward a word, etc.).

On Macs, the "Command" key (also on either side fo the spacebar) is used heavily in system shortcuts.  That means that care is needed to interpret it as a "Meta" key: Command-f is usually interpreted as "find," but Emacs uses it for "forward-word," for example.

The result was that I felt like I was constantly hitting the wrong keys, even after remapping keys or selecting Emacs bindings in my applications.  Worse, I started to feel like I was constantly dithering over the correct key in the correct context, which felt terrible in terms of maintaining focus on actual work.

# Vi to the rescue

I've noticed that applications I use tend to have fairly developed Vi modes, often supporting significantly more features than the Emacs modes.  I suspect that has something to do with the modal nature of Vi, since keystrokes in command mode can be interpreted by the mode itself.  My hypothesis is that using Vi bindings when possible will reduce friction between applications, and that using them uniformly will make learning faster.

So far, things seem to be going well.  I've switched to evil-mode in Spacemacs, vi mode in Bash, and VSCodeVim in VSCode.  I haven't done anything with Chrome, but it seems like there's some options for that as well.  After a few weeks, I'm getting better at navigation (which I find even better than Emacs), and am starting to get used to text manipulation.

# Tips

There's a few things I've already found that are very helpful

  * Karabiner-elements: I use this to 
    * Change Caps Lock to Esc if tapped and Ctrl if held.  I've found that super useful
    * Switch Alt and Windows/Menu keys when I use my external Microsoft keyboard.  For whatever reason, Alt gets mapped to Option instead of Command by default
