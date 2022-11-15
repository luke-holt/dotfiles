return require('packer').startup(function()
    use 'wbthomason/packer.nvim'
    use 'EdenEast/nightfox.nvim'
    use 'kyazdani42/nvim-web-devicons'
    use 'kyazdani42/nvim-tree.lua'
    use 'rcarriga/nvim-notify' -- fancy notifications
    use 'nvim-lualine/lualine.nvim' -- status line on bottom
    use 'romgrk/barbar.nvim' -- tab bar on top
    use {
        'windwp/nvim-autopairs',
        config = function() require('nvim-autopairs').setup{} end
    }

    -- treesitter for better syntax highlighting... among other things
    use {
        'nvim-treesitter/nvim-treesitter',
        run = function() require('nvim-treesitter.install').update({ with_sync = true }) end,
    }

    --> LSP plugins
    use 'neovim/nvim-lspconfig'
    use 'hrsh7th/nvim-cmp'  -- autocompletion plugin
    use 'hrsh7th/cmp-nvim-lsp' -- LSP source for nvim-cmp
    use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp
    use 'L3MON4D3/LuaSnip' -- Snippets plugin
    use 'onsails/lspkind-nvim' -- for icons in autocompletion
    use { 
        'lervag/vimtex',
        opt = true,
        config = function ()
            vim.g.vimtex_compiler_method = 'latexmk' -- default
            vim.g.vimtex_compiler_latexmk_engines = { _ = '-xelatex' }

            -- vim.g.vimtex_view_method = 'zathura'
            -- vim.g.vimtex_view_general_viewer = 'okular'
            -- vim.g.vimtex_compiler_latexmk_engines = { _ = '-xelatex' }
            -- vim.g.tex_comment_nospell = 1
            -- vim.g.vimtex_view_general_options = [[--unique file:@pdf\#src:@line@tex]]
            -- vim.g.vimtex_view_general_options_latexmk = '--unique'
        end,
        ft = 'tex'
    }
    use ({
        'jose-elias-alvarez/null-ls.nvim',
        requires = { 'nvim-lua/plenary.nvim' },
    })
end)
