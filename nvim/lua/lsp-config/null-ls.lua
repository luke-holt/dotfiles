local null_ls = require('null-ls')

local b = null_ls.builtins

local with_root_file = function(...)
    local files = { ... }
    return function(utils)
        return utils.root_has_file(files)
    end
end

local sources = {
    -- b.formatting.autopep8, -- python
    b.formatting.stylua.with({
        condition = with_root_file("stylua.toml"),
    }),
    b.formatting.dprint, -- rust
    b.formatting.black, -- python
    b.formatting.prettier,
    b.diagnostics.chktex, -- latex
}

null_ls.setup({
    sources = sources,
})

