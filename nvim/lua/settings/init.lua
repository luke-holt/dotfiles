local opt = vim.opt

vim.notify = require("notify")

opt.number = true
opt.relativenumber = true

opt.expandtab = false
opt.smarttab = true
opt.shiftwidth = 4
opt.tabstop = 4
opt.autoindent = true

opt.hlsearch = true
opt.incsearch = true
opt.ignorecase = true
opt.smartcase = true

opt.splitbelow = true
opt.splitright = true
opt.wrap = false
opt.scrolloff = 8
opt.fileencoding = 'utf-8'
opt.termguicolors = true

opt.hidden = true

opt.mouse = ''
